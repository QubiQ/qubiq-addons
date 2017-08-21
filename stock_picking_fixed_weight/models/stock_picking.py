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
"""

from openerp import models, fields, api
class stock_picking(models.Model):
	_inherit = 'stock.picking'

	weight_fixed = fields.Float(string='Weight')
"""



# Se ha escrito en la Api 7 por un bug de Odoo


from openerp.osv import fields,osv
from openerp.tools.translate import _

class stock_picking(osv.osv):
    _inherit = 'stock.picking'
    _columns = {

        
        'weight_fixed': fields.float(string=_('MODIFIED WEIGTH')),
        
    }

    # Sobre escritura completa de la función para tener en cuenta el precio fijo
    def _prepare_shipping_invoice_line(self, cr, uid, picking, invoice, context=None):
        """Prepare the invoice line to add to the shipping costs to the shipping's
           invoice.

            :param browse_record picking: the stock picking being invoiced
            :param browse_record invoice: the stock picking's invoice
            :return: dict containing the values to create the invoice line,
                     or None to create nothing
        """
        carrier_obj = self.pool.get('delivery.carrier')
        grid_obj = self.pool.get('delivery.grid')
        currency_obj = self.pool.get('res.currency')
        if not picking.carrier_id or \
            any(inv_line.product_id.id == picking.carrier_id.product_id.id
                for inv_line in invoice.invoice_line):
            return None
        grid_id = carrier_obj.grid_get(cr, uid, [picking.carrier_id.id],
                picking.partner_id.id, context=context)
        if not grid_id:
            raise osv.except_osv(_('Warning!'),
                    _('The carrier %s (id: %d) has no delivery grid!') \
                            % (picking.carrier_id.name,
                                picking.carrier_id.id))
        quantity = sum([line.product_uom_qty for line in picking.move_lines])
        # MODIFICACIÓN PARA PESO VOLUMETRICO - HEREDA DEL MODULO delivery
        weight=picking.weight 
        if (picking.weight_fixed) :
        	weight=picking.weight_fixed
        price = grid_obj.get_price_from_picking(cr, uid, grid_id,
                invoice.amount_untaxed, weight, picking.volume,
                quantity, context=context)
        # FIN MODIFICACION
        if invoice.company_id.currency_id.id != invoice.currency_id.id:
            price = currency_obj.compute(cr, uid, invoice.company_id.currency_id.id, invoice.currency_id.id,
                price, context=dict(context or {}, date=invoice.date_invoice))
        account_id = picking.carrier_id.product_id.property_account_income.id
        if not account_id:
            account_id = picking.carrier_id.product_id.categ_id\
                    .property_account_income_categ.id

        taxes = picking.carrier_id.product_id.taxes_id
        partner = picking.partner_id or False
        fp = invoice.fiscal_position or partner.property_account_position
        if partner:
            account_id = self.pool.get('account.fiscal.position').map_account(cr, uid, fp, account_id)
            taxes_ids = self.pool.get('account.fiscal.position').map_tax(cr, uid, fp, taxes, context=context)
        else:
            taxes_ids = [x.id for x in taxes]

        return {
            'name': picking.carrier_id.name,
            'invoice_id': invoice.id,
            'uos_id': picking.carrier_id.product_id.uos_id.id,
            'product_id': picking.carrier_id.product_id.id,
            'account_id': account_id,
            'price_unit': price,
            'quantity': 1,
            'invoice_line_tax_id': [(6, 0, taxes_ids)],
        }



   

stock_picking()








	