# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, api


class PaymentOrderCreate(models.TransientModel):
    _inherit = 'payment.order.create'

    @api.multi
    def filter_lines(self, lines):
        # Filter move lines according payment mode defined in the invoice
        self.ensure_one()
        res = super(PaymentOrderCreate, self).filter_lines(lines)
        final = []
        current_payment = self.env['payment.order'].browse(self.env.context['active_id'])
        for line_id in res:
            l = self.env['account.move.line'].browse(line_id)
            if l.stored_invoice_id.payment_mode_id == current_payment.mode:
                final.append(l.id)
        return final
