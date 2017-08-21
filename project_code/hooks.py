# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import SUPERUSER_ID


def create_code_equal_to_id(cr):
    """
    With this pre-init-hook we want to avoid error when creating the UNIQUE
    code constraint when the module is installed and before the post-init-hook
    is launched.
    """
    cr.execute('ALTER TABLE project_project '
               'ADD COLUMN project_code character varying;')
    cr.execute('UPDATE project_project '
               'SET project_code = id;')


def assign_old_sequences(cr, registry):
    """
    This post-init-hook will update all existing issue assigning them the
    corresponding sequence code.
    """
    project_obj = registry['project.project']
    sequence_obj = registry['ir.sequence']
    project_ids = project_obj.search(cr, SUPERUSER_ID, [], order="id")
    for project_id in project_ids:
        cr.execute('UPDATE project_project '
                   'SET project_code = \'%s\' '
                   'WHERE id = %d;' %
                   (sequence_obj.get(cr, SUPERUSER_ID, 'project.project'),
                    project_id))
