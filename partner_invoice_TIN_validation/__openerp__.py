# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Partner Invoice TIN Validation',
    'version': '8.0.1.0.0',
    'category': 'Account',
    'description': """
        This module adds the functionality to prevent invoice valition if the partner has no TIN information.
    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': [
        'account'
        ],
    'data': [
        'views/workflow.xml'
        ],
    'auto_install': False,
    'installable': True,
}
