# -*- coding: utf-8 -*-

{
    'name': 'Payment Information on Invoice Report',
    'version':'1.0',
    'category' : 'Custom',
    'description': """
        This module adds payment information (payment method and bank account) to the invoice report. If the payment method is bank receipt the bank account of the partner will be shown.
    """,
    'author':'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': ['base','account'],
    'data': [   'views/account_invoice_report.xml',
          ],
    'auto_install': False,
    'installable': True,
}

