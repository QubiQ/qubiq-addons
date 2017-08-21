# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api

# Change this variable if you need
maxim_fields = 400


class ir_actions_act_window(models.Model):
    _inherit = 'ir.actions.act_window'

    @api.model
    def change_all_limit_tree_views(self):
        action_objs = self.env['ir.actions.act_window'].search([
                        ('limit', '>', 0)])
        for action in action_objs:
            if action.limit > 0:
                action.limit = maxim_fields
