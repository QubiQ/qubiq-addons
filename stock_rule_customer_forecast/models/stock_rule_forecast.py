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


class stock_rule_forecast(models.Model):
    _name = "stock.rule.forecast"
    _description = (
        "It stores the orderpoint info for each customer/product "
        "report, and the linked lines of detail with the values of the ")

    product_template_id = fields.Many2one(
        comodel_name='product.template',
        string='Product', ondelete='set null', requiered=True, index=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner', string='Partner', requiered=True, index=True)
    company_id = fields.Many2one(
        comodel_name='res.company', string='Company', ondelete='cascade',
        required=True, readonly=False,
        default=lambda self: self.env.user.company_id.id)
    end_date = fields.Date(
        string='End Date')
    product_min_qty = fields.Float(string='Minimum Quantity', required=True,
                                   default=0)
    product_max_qty = fields.Float(string='Minimum Quantity', required=True,
                                   default=0)

    _sql_constraints = [
        ('stock_rule_forecast_uniq',
         'unique(product_template_id, partner_id,company_id)',
         _("Record duplicated!"))
    ]


