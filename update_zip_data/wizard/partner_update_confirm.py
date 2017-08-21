# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, api


class partner_update_confirm(models.TransientModel):
    """ Actualiazción de los datos de partner """
    _name = "partner.update.confirm"

    @api.multi
    def confirm(self):
        partner_domain = [
            ('zip', '!=', '')
        ]
        partner_obj = self.env['res.partner'].search(partner_domain)
        for o in partner_obj:
            if not o.state_id.id:
                zip_domain = [('name', '=', o.zip.strip())]
                zip_obj = self.env['res.better.zip'].search(zip_domain)
                for z in zip_obj:
                    o.write({
                        'zip_id': z.id,
                        'country_id': z.country_id.id,
                        'state_id': z.state_id.id,
                        'zip': z.name})
        return {'type': 'ir.actions.act_window_close'}
