# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Virtual Machine Manager',
    'version': '8.0.1.0.0',
    'category': 'Custom',
    'description': """
        This module allows the user to manage the information related to the
        virtual machines, such as name, partner, domain, port, etc.
    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends':  [
        'base'
        ],
    'data': [
        'views/virtual_machine_manager.xml',
        'security/ir.model.access.csv',
        ],
    'auto_install': False,
    'installable': True,
}
