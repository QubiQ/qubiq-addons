# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Product Order Point Auto Creation',
    'version': '1.0',
    'category': 'Custom',
    'description': """
Product Order Point Auto Creation
=================================

Create a new order point with 0 0 values everytime a new product is created

    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends':  ['stock', ],
    'auto_install': False,
    'installable': True,
    'post_init_hook': 'update_order_point',
}
