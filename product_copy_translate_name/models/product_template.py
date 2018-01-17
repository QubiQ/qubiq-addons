# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
from openerp import api, models
import logging


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    """
    Se sobreescribe para grabar directo en BBDD asi
    se sobreescribe el texto src de las traducciones.
    """
    @api.multi
    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        if 'name' in vals:
            self._cr.execute("""
                        update product_template
                        set name = %s
                        where id = %s;
                        """, (vals['name'], self.id))
        return res
