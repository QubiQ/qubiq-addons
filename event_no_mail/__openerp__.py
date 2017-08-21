# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Send No Email on Event',
    'version': '8.0.1.0.0',
    'category': 'Custom',
    'description': """
        This module adds a functionality that allows the user to choose if he
        wants to send an email to the attendees of an event.
    """,
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': [
        'base',
        'calendar'
        ],
    'data': [
                'views/calendar_event.xml',
            ],
    'auto_install': False,
    'installable': True,
}
