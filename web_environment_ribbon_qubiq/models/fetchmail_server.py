# -*- encoding: utf-8 -*-

from openerp import models, api


class fetchmail_server(models.Model):
    _inherit = 'fetchmail.server'

    @api.model
    def erase_all_mail_servers(self):
        mails = self.env['fetchmail.server'].search([])
        for mail in mails:
            mail.sudo().unlink()
