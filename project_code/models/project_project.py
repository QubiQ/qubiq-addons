# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import api, fields, models, _


class Project(models.Model):
    _inherit = 'project.project'

    project_code = fields.Char(
        string='Project Code', required=True, default="/", readonly=True)

    _sql_constraints = [
        ('project_project_unique_code', 'UNIQUE (project_code)',
         _('The code must be unique!')),
    ]

    @api.model
    def create(self, vals):
        if vals.get('project_code', '/') == '/':
            vals['project_code'] = self.env['ir.sequence'].get('project.project')
        return super(Project, self).create(vals)

    @api.one
    def copy(self, default=None):
        if default is None:
            default = {}
        default['project_code'] = self.env['ir.sequence'].get('project.project')
        return super(Project, self).copy(default)
