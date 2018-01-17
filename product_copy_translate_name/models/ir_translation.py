# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)


from openerp import fields, models


class IrTranslation(models.Model):
    _inherit = 'ir.translation'

    tra_ant = fields.Text(string="Traduccion antigua")
