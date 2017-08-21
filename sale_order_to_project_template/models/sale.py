# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    client_order_ref = fields.Char(required=True)

    @api.multi
    def action_button_confirm(self):
        proj_template_obj = self.env['project.project'].search([
                                        ('state', '=', 'template')
                                        ])
        if proj_template_obj:
            template_obj = proj_template_obj[0]
            dict_return = template_obj.duplicate_template()
            new_project_obj = self.env['project.project'].browse(
                                        dict_return['res_id'])
            new_dict = {
                        'name': self.name + ' / ' + self.client_order_ref,
                        'partner_id': self.partner_id.id
                        }
            new_project_obj.write(new_dict)
            self.project_id = new_project_obj.analytic_account_id
        return super(SaleOrder, self).action_button_confirm()
