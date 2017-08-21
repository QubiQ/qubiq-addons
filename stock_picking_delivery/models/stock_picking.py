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

from openerp import models, fields, api, _
from openerp.osv import osv

class delivery_grid(models.Model):
    _inherit = 'delivery.grid'

    def get_prices_from_picking(self, cr, uid, id, total, weight, volume, quantity, context=None):
        grid = self.browse(cr, uid, id, context=context)
        price = 0.0
        res = []
        ok = False
        price_dict = {'price': total, 'volume':volume, 'weight': weight, 'wv':volume*weight, 'quantity': quantity}
        for line in grid.line_ids:
            test = eval(line.type+line.operator+str(line.max_value), price_dict)
            if test:
                if line.price_type=='variable':
                    res.append(line.list_price)
                    res.append(line.standard_price)
                else:
                    res.append(line.list_price)
                    res.append(line.standard_price)
                ok = True
                break
        if not ok:
            raise osv.except_osv(_("Unable to fetch delivery method!"), _("Selected product in the delivery method doesn't fulfill any of the delivery grid(s) criteria."))

        return res


class stock_picking(models.Model):
    _inherit = 'stock.picking'
    precio_coste_transporte = fields.Float(copy=False,store=True)
    precio_venta_transporte = fields.Float(copy=False,store=True)

    def _prepare_shipping_invoice_line(self, cr, uid, picking, invoice, context=None):
        res = super(stock_picking,self)._prepare_shipping_invoice_line(cr, uid, picking, invoice, context)
        if res:
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
	        price = grid_obj.get_prices_from_picking(cr, uid, grid_id,
	                invoice.amount_untaxed, picking.weight, picking.volume,
	                quantity, context=context)
	        picking.precio_venta_transporte = price[0]
	        picking.precio_coste_transporte = price[1]
        return res

        









    

