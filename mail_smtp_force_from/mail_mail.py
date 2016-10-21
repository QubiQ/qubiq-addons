# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    ThinkOpen Solutions Brasil
#    Copyright (C) Thinkopen Solutions <http://www.tkobr.com>.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.addons.base.ir.ir_mail_server import extract_rfc2822_addresses
from openerp.osv import osv, fields


class ir_mail_server(osv.osv):
    _inherit = 'ir.mail_server'


    def send_email(self, cr, uid, message, mail_server_id=None, smtp_server=None, smtp_port=None, smtp_user=None,
                   smtp_password=None, smtp_encryption=None, smtp_debug=False, context=None):
        
                                            
        server_obj=self.pool.get('ir.mail_server')
        server_id = server_obj.search(cr, uid, [],context=context)       
        
        if server_id and server_id[0]:
            smtp_server_obj=server_obj.browse(cr, uid,server_id[0],context=context)           
            
            message['Return-Path'] = smtp_server_obj['smtp_user']
          

        return super(ir_mail_server, self).send_email(cr, uid, message, mail_server_id, smtp_server, smtp_port,
                                                      smtp_user, smtp_password, smtp_encryption, smtp_debug,
                                                      context=context)




