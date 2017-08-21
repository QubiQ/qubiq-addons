# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

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
