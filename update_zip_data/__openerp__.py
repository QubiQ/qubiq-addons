# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Update ZIP Data',
    'version': '1.0',
    'category': 'Custom',
    'description': """
      Update all the partners with ZIP data.
      Creates a menu on Sales -> Configuration.
      The module can be uninstalled once the data has been updated.
    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': [],
    'data': [
         'wizard/partner_update_confirm.xml',
          ],
    'auto_install': False,
    'installable': True,
}
