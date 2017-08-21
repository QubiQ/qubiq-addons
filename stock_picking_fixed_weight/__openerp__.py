# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    'name': 'Add Weight Stock Picking',
    'version': '8.0.1.0.0',
    'category': 'Stock',
    'description': """
        Modulo que permite poner el peso manualmente en albaran de salida
    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': [
        'stock',
        'delivery'
        ],
    'data': [
        'wizard/stock_picking_change_weight.xml',
        'views/stock_picking_view.xml',
        ],
    'auto_install': False,
    'installable': True,
}
