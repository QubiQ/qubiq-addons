# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)

from openerp.osv import osv


class res_partner(osv.osv):
    _inherit = 'res.partner'

    def check_vat(self, cr, uid, ids, context=None):
        return True

    def _construct_constraint_msg(self, cr, uid, ids, context=None):
        return True

    def button_check_vat(self, cr, uid, ids, context=None):
        return True

    def simple_vat_check(self, cr, uid, country_code, vat_number, context=None):
        return True

    _constraints = []
    __check_vat_ch_re1 = []
    __check_vat_ch_re2 = []


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
