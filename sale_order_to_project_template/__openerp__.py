# -*- coding: utf-8 -*-

{
    'name': 'Sale Order to project template',
    'version':'1.0',
    'category' : 'Sales',
    'description': """
        This module adds a functionality that allows the user to create a project according a template when the sales order is confirmed.

        Make sure the  "Analytic accounting for sales" is checked. (Settings --> Configuration --> Invoicing -->Analytic Accounting ) 
    """,
    'author':'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': ['sale','project','account'],
    'data': [
           
            'views/sale_order.xml',
            ],
    'auto_install': False,
    'installable': True,
}

