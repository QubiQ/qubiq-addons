# -*- coding: utf-8 -*-

from openerp import models, fields, _

class module_model(models.Model):
	_name = 'module.model'
	
	name = fields.Char(string=_("Module Name"), required=True)

class project_task(models.Model):
	_inherit = 'project.task'

	module_id = fields.Many2one(comodel_name='module.model', string=_("Module Name"))

class project_issue(models.Model):
	_inherit = 'project.issue'

	module_id = fields.Many2one(comodel_name='module.model', string=_("Module Name"))






