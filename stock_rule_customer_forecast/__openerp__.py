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
    'name': 'Stock rule customer forecast',
    'version': '8.0.0.1.0',
    'sequence': 14,
    'summary': 'stock',
    'description': """
Stock rule customer forecast
=============================

Define stock rules in product or customer form whith a validity date.
Create a wizard to update orderpoints according the information definied in the product or customer form

# Project Qubiq Github. Branch #Stock_rule_customer_forecast


    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': ['product','sale','stock'],
    'category': 'stock',
    'data': [
            "security/ir.model.access.csv",
            "views/product_template.xml",
             "views/res_partner.xml",],
    'demo': [],
    'installable': True,
}