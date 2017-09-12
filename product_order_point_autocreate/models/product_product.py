# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, api
import logging

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def create(self, vals=None):
        rec = super(ProductProduct, self).create(vals)
        regla_obj = self.env['stock.warehouse.orderpoint']
        if rec.type == 'product':
            res = regla_obj.default_get({'company_id'})
            _logger.info('Creando Regla de stock para producto :'+str(
                            rec.default_code))

            regla_obj.create({'warehouse_id': res['warehouse_id'],
                              'location_id': res['location_id'],
                              'product_id': rec.id,
                              'product_min_qty': 0,
                              'product_max_qty': 0,
                              'qty_multiple': 0,
                              })
        return rec
