# -*- coding: utf-8 -*-

{
    'name': 'Mass Mailing on Specified Date',
    'version':'1.0',
    'category' : 'Mail',
    'description': """
        This module adds a functionality that allows the user to send mass mails on a specified date. It uses a cron that checks daily if there are mails ready to be sent.
    """,
    'author':'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': ['mass_mailing'],
    'data': [
            'data/cron.xml',
            'views/mass_mailing.xml',
            ],
    'auto_install': False,
    'installable': True,
}

