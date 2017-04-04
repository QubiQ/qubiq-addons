# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-Today OpenERP SA (<http://www.openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Bank Statement Validation State',
    'version': '8.0.1.0.0',
    'sequence': 14,
    'summary': 'Account',
    'description': """
            New state validation in bank statement.
    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': ['base',
                'account',
                ],
    'category': 'Account',
    'data': [
             'views/account_view.xml',
             ],
    'demo': [],
    'installable': True,
}
