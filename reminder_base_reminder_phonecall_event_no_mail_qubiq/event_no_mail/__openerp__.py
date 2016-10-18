# -*- coding: utf-8 -*-

{
    'name': 'Event no mail',
    'version':'1.0',
    'category' : 'Custom',
    'description': """
        Módulo el cual añade un checkbox en eventos el cual controla el envio de mails a los asistentes.
    """,
    'author':'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': ['base','calendar','reminder_base','reminder_phonecall'],
    'data': [   
                'views/calendar_event.xml',
            ],
    'auto_install': False,
    'installable': True,
}

