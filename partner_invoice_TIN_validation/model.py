# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, api, _
from openerp.exceptions import Warning


class account_invoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def nif_validate(self):
        if self.partner_id.vat:
            self.signal_workflow('invoice_open')
        else:
            raise Warning(_("The partner needs a valid TIN."))
