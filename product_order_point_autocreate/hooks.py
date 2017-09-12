# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import api, SUPERUSER_ID
import logging
_logger = logging.getLogger(__name__)


def update_order_point(cr, registry):
    """Put domain in product access rule and copy company_id as the default
    value in new field company_ids."""
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        products = env['product.product'].search([('type', '=', 'product')])
        for product in products:
            regla_obj = env['stock.warehouse.orderpoint'].search([
                    ('product_id', '=', product.id)])
            if not regla_obj:
                res = regla_obj.default_get({'company_id'})
                _logger.info('Creando Regla de stock para producto :'+str(
                        product.default_code))

                regla_obj.create({'warehouse_id': res['warehouse_id'],
                                  'location_id': res['location_id'],
                                  'product_id': product.id,
                                  'product_min_qty': 0,
                                  'product_max_qty': 0,
                                  'qty_multiple': 0,
                                  })
