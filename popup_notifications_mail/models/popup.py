# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields, api
from openerp.tools import html_email_clean


class popup_notification(models.Model):
    _name = "popup.notification"

    title = fields.Char()
    message = fields.Text()
    status = fields.Selection([('shown', 'shown'), ('draft', 'draft')], defaul='draft')
    partner_ids = fields.Many2many('res.users')

    @api.multi
    def get_notifications(self):
        result = []
        for obj in self:
            result.append({
                'title': obj.title,
                'message': obj.message,
                'status': obj.status,
                'id': obj.id,
            })
        return result


class mail_notification(models.Model):
    _inherit = 'mail.message'

    is_notified = fields.Boolean(string='Notified', default=False)

    @api.model
    def _cron_search_notifications_not_notified(self):
        url = self.sudo().env['ir.config_parameter'].search([('key', '=', 'url_web_notifications')])[0].value
        texto_a_borrar = """<hr tabindex="-1" style="display:inline-block; width:98%"/><span>&#13;"""
        texto_link_base = """<a href="#" class="oe_mail_expand">leer m&#225;s</a>"""
        print "OK1"
        res_users = self.sudo().env['res.users'].search([('id', '!=', '-1')])
        print "OK2"
        for res_user in res_users:
            p_id = res_user.partner_id.id
            sql = """
                select mm2.id as id
                from mail_message mm1
                INNER JOIN mail_message mm2 ON mm2.parent_id = mm1.id
                where mm1.author_id = cast(%s as int) and mm2.type = 'email' and mm2.is_notified = False
                order by id desc
            """
            self._cr.execute(sql, (p_id,))
            print p_id
            res = self._cr.dictfetchall()
            ids = []
            for r in res:
                ids.append(int(r['id']))
                print r
            for message_obj in self.env['mail.message'].search([('id', 'in', ids)]):
                txt = html_email_clean(message_obj.body, remove=True, shorten=True, max_length=40)
                txt = txt[:txt.find(texto_a_borrar)]
                pos_texto_link_base = txt.find(texto_link_base)
                if pos_texto_link_base > -1:
                    href = url+'id='+str(message_obj.res_id)+'&view_type=form&model='+str(message_obj.model)
                    txt = txt[:pos_texto_link_base]+"<a href=\""+href+"\" class=\"oe_mail_expand\">leer m&#225;s</a>"+txt[pos_texto_link_base+52:]
                values = {
                        'status': 'draft',
                        'title': message_obj.email_from+'\n'+message_obj.subject,
                        'message': txt,
                        'partner_ids': [(6, 0, [res_user.id])]}
                self.env['popup.notification'].create(values)
                message_obj.is_notified = True
