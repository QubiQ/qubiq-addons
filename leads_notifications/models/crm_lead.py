# -*- coding: utf-8 -*-

from openerp import models, api

class crm_lead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def _needaction_domain_get(self):
        return [('user_id', '=', False)]