# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp.addons.base.ir.ir_mail_server import extract_rfc2822_addresses
from openerp.osv import osv


class ir_mail_server(osv.osv):
    _inherit = 'ir.mail_server'

    def send_email(self, cr, uid, message, mail_server_id=None,
                   smtp_server=None, smtp_port=None, smtp_user=None,
                   smtp_password=None, smtp_encryption=None,
                   smtp_debug=False, context=None):

        server_obj = self.pool.get('ir.mail_server')
        server_id = server_obj.search(cr, uid, [], context=context)

        if server_id and server_id[0]:
            smtp_server_obj = server_obj.browse(cr, uid,
                                                server_id[0], context=context)
            message['Return-Path'] = smtp_server_obj['smtp_user']
        return super(ir_mail_server, self).send_email(cr, uid, message,
                                                      mail_server_id,
                                                      smtp_server, smtp_port,
                                                      smtp_user, smtp_password,
                                                      smtp_encryption,
                                                      smtp_debug,
                                                      context=context)
