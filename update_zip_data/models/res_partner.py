# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2012 OpenERP SA (<http://openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
import string
import datetime
import re
from openerp.osv import fields, osv
from openerp.tools.misc import ustr
from openerp.tools.translate import _
_logger = logging.getLogger(__name__)


class res_partner(osv.osv):
    _inherit = 'res.partner'

    

    def check_vat(self, cr, uid, ids, context=None):
    	       
        return True

    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
