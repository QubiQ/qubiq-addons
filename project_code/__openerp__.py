# -*- coding: utf-8 -*-


{
    "name": "Project Code",
    "version": "8.0.1.0.0",
    'author': 'QubiQ',
    "category": "Project Management",
    'summary': 'Adding Field Code For Project',
    'website': 'https://www.qubiq.es',
    "license": "AGPL-3",
    "depends": [
        "project",
    ],
    "data": [
        "data/project_sequence.xml",
        "views/project_view.xml",
    ],
    "installable": True,
    "pre_init_hook": "create_code_equal_to_id",
    "post_init_hook": "assign_old_sequences",
}
