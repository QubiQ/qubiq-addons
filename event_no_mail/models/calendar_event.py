# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
import pytz
import re
import time
import openerp
import openerp.service.report
import uuid
import collections
import babel.dates
from werkzeug.exceptions import BadRequest
from datetime import datetime, timedelta
from dateutil import parser
from dateutil import rrule
from dateutil.relativedelta import relativedelta
from openerp import api
from openerp import tools, SUPERUSER_ID
from openerp.osv import fields, osv
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from openerp.tools.translate import _
from openerp.http import request
from operator import itemgetter
import unicodedata

class calendar_attendee(osv.Model):
    """
    Calendar Attendee Information
    """
    _inherit = 'calendar.attendee'

    _columns = {
                'envio_mail': fields.boolean('Send email'),
                }
    _defaults = {
                'envio_mail': True,
                }


    def _send_mail_to_attendees(self, cr, uid, ids, email_from=tools.config.get('email_from', False),
                                template_xmlid='calendar_template_meeting_invitation', force=False, context=None):
        """
        Send mail for event invitation to event attendees.
        @param email_from: email address for user sending the mail
        @param force: If set to True, email will be sent to user himself. Usefull for example for alert, ...
        """
        res = False

        if self.pool['ir.config_parameter'].get_param(cr, uid, 'calendar.block_mail', default=False) or context.get("no_mail_to_attendees"):
            return res

        mail_ids = []
        data_pool = self.pool['ir.model.data']
        mailmess_pool = self.pool['mail.message']
        mail_pool = self.pool['mail.mail']
        template_pool = self.pool['email.template']
        local_context = context.copy()
        color = {
            'needsAction': 'grey',
            'accepted': 'green',
            'tentative': '#FFFF00',
            'declined': 'red'
        }

        if not isinstance(ids, (tuple, list)):
            ids = [ids]

        dummy, template_id = data_pool.get_object_reference(cr, uid, 'calendar', template_xmlid)
        dummy, act_id = data_pool.get_object_reference(cr, uid, 'calendar', "view_calendar_event_calendar")
        local_context.update({
            'color': color,
            'action_id': self.pool['ir.actions.act_window'].search(cr, uid, [('view_id', '=', act_id)], context=context)[0],
            'dbname': cr.dbname,
            'base_url': self.pool['ir.config_parameter'].get_param(cr, uid, 'web.base.url', default='http://localhost:8069', context=context)
        })

        for attendee in self.browse(cr, uid, ids, context=context):

            if attendee.envio_mail and attendee.email and email_from and (attendee.email != email_from or force): # cambiada.
                ics_file = self.get_ics_file(cr, uid, attendee.event_id, context=context)
                mail_id = template_pool.send_mail(cr, uid, template_id, attendee.id, context=local_context)

                vals = {}
                if ics_file:
                    vals['attachment_ids'] = [(0, 0, {'name': 'invitation.ics',
                                                      'datas_fname': 'invitation.ics',
                                                      'datas': str(ics_file).encode('base64')})]
                vals['model'] = None  # We don't want to have the mail in the tchatter while in queue!
                the_mailmess = mail_pool.browse(cr, uid, mail_id, context=context).mail_message_id
                mailmess_pool.write(cr, uid, [the_mailmess.id], vals, context=context)
                mail_ids.append(mail_id)

        if mail_ids:
            res = mail_pool.send(cr, uid, mail_ids, context=context)

        return res



class calendar_event(osv.Model):

    _inherit = "calendar.event"

    _columns = {
                'envio_mail': fields.boolean('Send email'),
                }
    _defaults = {
                'envio_mail': True,
                }


    def write(self, cr, uid, ids, values, context=None):
        context = context or {}
        if not isinstance(ids, (tuple, list)):
            ids = [ids]

        values0 = values
        envent_objs = self.pool['calendar.event']
        # process events one by one
        for event_id in ids:
            envio_mail = envent_objs.browse(cr, uid, event_id, context=context).envio_mail
            # make a copy, since _set_date() modifies values depending on event
            values = dict(values0)
            self._set_date(cr, uid, values, event_id, context=context)

            # special write of complex IDS
            real_ids = []
            new_ids = []
            if '-' not in str(event_id):
                real_ids = [int(event_id)]
            else:
                real_event_id = calendar_id2real_id(event_id)

                # if we are setting the recurrency flag to False or if we are only changing fields that
                # should be only updated on the real ID and not on the virtual (like message_follower_ids):
                # then set real ids to be updated.
                blacklisted = any(key in values for key in ('start', 'stop', 'active'))
                if not values.get('recurrency', True) or not blacklisted:
                    real_ids = [real_event_id]
                else:
                    data = self.read(cr, uid, event_id, ['start', 'stop', 'rrule', 'duration'])
                    if data.get('rrule'):
                        new_ids = [self._detach_one_event(cr, uid, event_id, values, context=None)]

            super(calendar_event, self).write(cr, uid, real_ids, values, context=context)

            # set end_date for calendar searching
            if values.get('recurrency') and values.get('end_type', 'count') in ('count', unicode('count')) and \
                    (values.get('rrule_type') or values.get('count') or values.get('start') or values.get('stop')):
                for id in real_ids:
                    final_date = self._get_recurrency_end_date(cr, uid, id, context=context)
                    super(calendar_event, self).write(cr, uid, [id], {'final_date': final_date}, context=context)

            attendees_create = False
            if values.get('partner_ids', False):
                attendees_create = self.create_attendees(cr, uid, real_ids + new_ids, context)


            if (values.get('start_date') or values.get('start_datetime')) and values.get('active', True):
                for the_id in real_ids + new_ids:
                    if attendees_create:
                        attendees_create = attendees_create[the_id]
                        mail_to_ids = list(set(attendees_create['old_attendee_ids']) - set(attendees_create['removed_attendee_ids']))
                    else:
                        mail_to_ids = [att.id for att in self.browse(cr, uid, the_id, context=context).attendee_ids]

                    if mail_to_ids and envio_mail: #Cambio en esta linea
                        current_user = self.pool['res.users'].browse(cr, uid, uid, context=context)
                        if self.pool['calendar.attendee']._send_mail_to_attendees(cr, uid, mail_to_ids, template_xmlid='calendar_template_meeting_changedate', email_from=current_user.email, context=context):
                            self.message_post(cr, uid, the_id, body=_("A email has been send to specify that the date has been changed !"), subtype="calendar.subtype_invitation", context=context)

        return True


    def create_attendees(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        user_obj = self.pool['res.users']
        current_user = user_obj.browse(cr, uid, uid, context=context)
        res = {}
        for event in self.browse(cr, uid, ids, context):
            attendees = {}
            for att in event.attendee_ids:
                attendees[att.partner_id.id] = True
            new_attendees = []
            new_att_partner_ids = []
            for partner in event.partner_ids:
                if partner.id in attendees:
                    continue
                access_token = self.new_invitation_token(cr, uid, event, partner.id)
                values = {
                    'partner_id': partner.id,
                    'event_id': event.id,
                    'access_token': access_token,
                    'email': partner.email,
                    'envio_mail':event.envio_mail,
                    'state': 'needsAction',
                }

                if partner.id == current_user.partner_id.id:
                    values['state'] = 'accepted'

                att_id = self.pool['calendar.attendee'].create(cr, uid, values, context=context)
                new_attendees.append(att_id)
                new_att_partner_ids.append(partner.id)

                if not current_user.email or current_user.email != partner.email:
                    mail_from = current_user.email or tools.config.get('email_from', False)
                    if not context.get('no_email'):
                        if self.pool['calendar.attendee']._send_mail_to_attendees(cr, uid, att_id, email_from=mail_from, context=context):
                            self.message_post(cr, uid, event.id, body=_("An invitation email has been sent to attendee %s") % (partner.name,), subtype="calendar.subtype_invitation", context=context)

            if new_attendees:
                self.write(cr, uid, [event.id], {'attendee_ids': [(4, att) for att in new_attendees]}, context=context)

            if new_att_partner_ids and event.envio_mail: # Cambio en esta linea.
                self.message_subscribe(cr, uid, [event.id], new_att_partner_ids, context=context)

            # We remove old attendees who are not in partner_ids now.
            all_partner_ids = [part.id for part in event.partner_ids]
            all_part_attendee_ids = [att.partner_id.id for att in event.attendee_ids]
            all_attendee_ids = [att.id for att in event.attendee_ids]
            partner_ids_to_remove = map(lambda x: x, set(all_part_attendee_ids + new_att_partner_ids) - set(all_partner_ids))

            attendee_ids_to_remove = []

            if partner_ids_to_remove:
                attendee_ids_to_remove = self.pool["calendar.attendee"].search(cr, uid, [('partner_id.id', 'in', partner_ids_to_remove), ('event_id.id', '=', event.id)], context=context)
                if attendee_ids_to_remove:
                    self.pool['calendar.attendee'].unlink(cr, uid, attendee_ids_to_remove, context)

            res[event.id] = {
                'new_attendee_ids': new_attendees,
                'old_attendee_ids': all_attendee_ids,
                'removed_attendee_ids': attendee_ids_to_remove
            }
        return res

















