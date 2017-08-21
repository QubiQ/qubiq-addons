# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp.osv import osv


class res_partner(osv.osv):
    _inherit = 'res.partner'

    def check_vat(self, cr, uid, ids, context=None):
        return True


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
