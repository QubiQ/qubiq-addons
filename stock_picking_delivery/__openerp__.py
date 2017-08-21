# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Stock Picking Delivery',
    'version': '8.0.1.0.0',
    'sequence': 14,
    'summary': 'stock',
    'description': """
Stock picking delivery
=============================
Crea el precio de coste del transporte en el albarán:
* Precio de coste del transporte

    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': [
        'sale',
        'stock',
        'delivery'
        ],
    'category': 'stock',
    'data': [],
    'demo': [],
    'installable': True,
}
