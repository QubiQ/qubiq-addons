# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)

{
    'name': 'Create Mandate',
    'version': '9.0.1.0.0',
    'category': 'Custom',
    'description': """
      Creating bank mandates for the partners that are clients, this module is prepared for the multicompany.
      You can choose whether you require the creation of bank mandates for all bank accounts or only those that do not have any associated banking mandate.
      The menu item is in:
      Sales -> Configuration -> Bank Accounts -> Creating Mandates
    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': [
          'account',
          'account_accountant',
                ],
    'data': [
         'wizard/mandate_create_confirm.xml',
            ],
    'external_dependencies': {
          'python': ['unicodecsv'],
    },
    'auto_install': False,
    'installable': True,
}
