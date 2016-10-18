# -*- coding: utf-8 -*-

{
    'name': 'Add Weight Stock Picking',
    'version':'1.0',
    'category' : 'Stock',
    'description': """
        Modulo que permite poner el peso manualmente en albaran de salida
            

    """,
    'author':'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': ['stock','delivery'],
    'data': [
        'wizard/stock_picking_change_weight.xml',
        'views/stock_picking_view.xml',
        ],
    'auto_install': False,
    'installable': True,
}

