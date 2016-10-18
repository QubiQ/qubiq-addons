# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp import models, api,fields
from datetime import datetime, timedelta,date 


class partner_update_confirm(models.TransientModel):
    """ Actualiazción de los datos de partner """
    _name = "partner.update.confirm"

    

    @api.multi
    def confirm(self):


        partner_domain = [
            
            ('zip', '!=', '')
        ]

        partner_obj = self.env['res.partner'].search(partner_domain)

        for o in partner_obj :
            if o.state_id.id==False:
                zip_domain=[('name','=',o.zip.strip())]
                zip_obj=self.env['res.better.zip'].search(zip_domain)
                for z in zip_obj :
                    o.write({'zip_id': z.id,'city': z.city,'country_id': z.country_id.id,'state_id':z.state_id.id,'zip':z.name})
        
        return {'type': 'ir.actions.act_window_close'}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
