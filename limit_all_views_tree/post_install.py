# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import SUPERUSER_ID


def set_default_initiating_party(cr, pool):
    pool['ir.actions.act_window'].change_all_limit_tree_views(cr, SUPERUSER_ID)
