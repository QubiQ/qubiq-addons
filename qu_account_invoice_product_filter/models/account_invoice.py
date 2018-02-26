# -*- coding: utf-8 -*-

from openerp import models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'
    product_id = fields.Many2one('product.product',
                                 related='invoice_line.product_id',
                                 string='Product')
