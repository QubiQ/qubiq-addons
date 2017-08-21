# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Payment Dates on Account Invoice',
    'version': '8.0.1.0.0',
    'category': 'Account',
    'description': """
        This module adds the due dates to the invoices.
    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': [
        'account',
        ],
    'data': [
        'views/report_invoice_layouted.xml',
        ],
    'auto_install': False,
    'installable': True,
}
