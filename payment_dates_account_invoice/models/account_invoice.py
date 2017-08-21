# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields
from datetime import datetime


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    due_dates_str = fields.Char(string="Due dates",
                                compute='_get_due_dates_str')

    def _get_due_dates(self):
        if self.date_invoice:
            pterm = self.env['account.payment.term'].browse(self.payment_term.id)
            pterm_list = pterm.compute(value=self.amount_total,
                                       date_ref=self.date_invoice)
            final_list = []
            if pterm_list[0]:
                for line in pterm_list[0]:
                    d = datetime.strptime(line[0], '%Y-%m-%d')
                    final_list.append((datetime.strftime(d, "%d/%m/%Y"), str(line[1]), self.currency_id.symbol), )
                return final_list
        else:
            return ''

    def _get_due_dates_str(self):
        if self.date_invoice:
            pterm = self.env['account.payment.term'].browse(self.payment_term.id)
            pterm_list = pterm.compute(value=self.amount_total,
                                       date_ref=self.date_invoice)
            final_str = ""
            if pterm_list[0]:
                for line in pterm_list[0]:
                    d = datetime.strptime(line[0], '%Y-%m-%d')
                    final_str = final_str+' '+(datetime.strftime(d, "%d/%m/%Y"))
            self.due_dates_str = final_str
        else:
            self.due_dates_str = False
