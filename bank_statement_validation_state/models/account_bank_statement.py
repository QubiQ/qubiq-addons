# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields, api


class account_bank_statement(models.Model):
    _inherit = 'account.bank.statement'
    state = fields.Selection([
                                ('draft', 'New'),
                                ('open', 'Open'),  # used by cash statements
                                ('completo', 'Finished'),
                                ('confirm', 'Closed')
                                ], 'Status', required=True, readonly="1", copy=False,
                                help='When new statement is created the status will be \'Draft\'.\n'
                                  'And after getting confirmation from the bank it will be in \'Confirmed\' status.')
    # state = fields.Selection(selection_add=[('completo', 'Completo')])

    @api.multi
    def button_draft(self):
        for sel in self:
            sel.state = 'draft'
        return True

    @api.multi
    def button_completo(self):
        for sel in self:
            sel.state = 'completo'
        return True
