# -*- coding: utf-8 -*-

{
    'name': 'Send No Email on Event',
    'version':'1.0',
    'category' : 'Custom',
    'description': """
        This module adds a functionality that allows the user to choose if he wants to send an email to the attendees of an event.
    """,
    'author':'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': ['base','calendar'],
    'data': [   
                'views/calendar_event.xml',
            ],
    'auto_install': False,
    'installable': True,
}

