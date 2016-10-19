# -*- coding: utf-8 -*-

{
    'name': 'Show Module Name on Tasks and Issues',
    'version':'1.0',
    'category' : 'Custom',
    'description': """
        This module adds a field that allows the user to insert the module name related to the task or issue.
    """,
    'author':'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends':  [   'base', 
                    'project',
                    'project_issue'
                ],
    'data': [   'views/show_module_name.xml',   ],
    'auto_install': False,
    'installable': True,
}

