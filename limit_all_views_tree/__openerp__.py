# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "limit all views tree",
    'version': '8.0.1.0.0',
    'category': 'Web',
    'author': 'Qubiq',
    'website': 'https://www.qubiq.es',
    'license': 'AGPL-3',
    "depends": [
        'web',
        'base',
        ],
    "data": [
        ],
    "update_xml": [],
    "demo_xml": [],
    'post_init_hook': 'set_default_initiating_party',
    "auto_install": False,
    "installable": True,
}
