# -*- encoding: utf-8 -*-

from openerp import models, api


class ir_mail_server(models.Model):
    _inherit = 'ir.mail_server'

    @api.model
    def erase_all_mail_servers(self):
        mails = self.env['ir.mail_server'].search([])
        for mail in mails:
            mail.sudo().unlink()
