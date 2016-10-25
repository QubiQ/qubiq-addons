# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2013 Camptocamp SA
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

from openerp import models, fields, api
from openerp.exceptions import except_orm
from openerp.tools.translate import _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    client_order_ref = fields.Char(required=True)

    

    @api.multi
    def action_button_confirm(self):
    	
    	proj_template_obj=self.env['project.project'].search([('state','=','template')])
    	if proj_template_obj :
    		template_obj=proj_template_obj[0]
    		dict_return=template_obj.duplicate_template()
    		new_project_obj=self.env['project.project'].browse(dict_return['res_id'])
    		new_dict={'name': self.name +' / '+self.client_order_ref,
    				  'partner_id' : self.partner_id.id }
    		new_project_obj.write(new_dict)
    		self.project_id=new_project_obj.analytic_account_id
    	return super(SaleOrder, self).action_button_confirm()

        
       

  
