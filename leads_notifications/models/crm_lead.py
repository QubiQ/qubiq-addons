# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, api


class crm_lead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def _needaction_domain_get(self):
        return [('user_id', '=', False)]
