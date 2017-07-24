# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from openerp import tools, SUPERUSER_ID








class CalendarAttendee(models.Model):
    _inherit = 'calendar.attendee'

    envio_mail = fields.Boolean(string='Send Mail', default=False)

    def _send_mail_to_attendees(self, email_from=tools.config.get(
        'email_from', False),
            template_xmlid='calendar_template_meeting_invitation', force=False,
            context=None):

        return super(CalendarAttendee, self.filtered(
            "envio_mail"))._send_mail_to_attendees(
                email_from, template_xmlid, force)


class CalendarEvent(models.Model):

    _inherit = "calendar.event"

    envio_mail = fields.Boolean(string='Send Mail', default=True)




    def write(self, values):
        return super(calendar_event,self.filtered("envio_mail")).write(values)



    def create_attendees(self):
        # TODO FALTA MIRAR COMO ELIMINAMOS LOS SUBSCRIPTION
        """
        if new_att_partner_ids and event.envio_mail: # Cambio en esta linea.
                self.message_subscribe(cr, uid, [event.id], new_att_partner_ids, context=context)
        Parece que tenemos que sobreescribir esta funcion i si new_att_partner_ids esta

        Pordemos ejecutar el messaage_unsubscribe para los partners (atendes igual a false)
        """

        result=super(calendar_event,self).create_attendees()
        
        event_obj=self.env['calendar.event'].browse(result.getKeys())
        for event in event_obj :
            event.attendee_ids.envio_mail=event.envio_mail

        return result










    
