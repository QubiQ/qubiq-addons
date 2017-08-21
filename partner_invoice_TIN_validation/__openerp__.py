# -*- coding: utf-8 -*-

{
    'name': 'Partner Invoice TIN Validation',
    'version':'1.0',
    'category' : 'Account',
    'description': """
        This module adds the functionality to prevent invoice valition if the partner has no TIN information.
    """,
    'author':'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': ['account'],
    'data': ['views/workflow.xml'],
    'auto_install': False,
    'installable': True,
}

