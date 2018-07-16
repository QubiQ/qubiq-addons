# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import api, models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat_revision = fields.Boolean(
        default=False,
        readonly=True,
        string=_('Needs VAT revision')
    )

    """
    Process to add ES ahead spanish customers's VAT
    """
    @api.multi
    def update_spanish_vat(self):
        country_id = self.env['res.country'].search([
            ('code', '=', 'ES')
            ]).id
        for partner in self.env['res.partner'].search([
            ('country_id', '=', country_id),
            ('vat', '!=', False),
            ('vat', '!=', '')
           ]):
            try:
                if partner.vat[:2] != 'ES':
                    partner.vat = 'ES' + partner.vat
            except:
                partner.vat_revision = True
