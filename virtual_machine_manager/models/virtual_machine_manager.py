# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields, _


class virtual_machine_information(models.Model):
    _name = 'virtual.machine.info'

    name = fields.Char(string=_("Amazon Machine Name"), required=True)
    ram = fields.Integer(string=_("RAM"))
    cores = fields.Integer(string=_("Cores"))
    amazon_instance_type = fields.Char(string=_("Amazon Instance Type"))
    version = fields.Selection(string=_("Odoo Version"), selection=([
                                                                ('7', '7.0'),
                                                                ('8', '8.0'),
                                                                ('9', '9.0'),
                                                                ('10', '10.0'),
                                                                ('11', '11.0'),
                                                                ('12', '12.0'),
                                                                ('13', '13.0'),
                                                                ('14', '14.0'),
                                                                    ]))

    _sql_constraints = [
        ('name_uniq',
         'UNIQUE(name)',
         _("Name already exists")),
    ]


class virtual_machine_partners(models.Model):
    _name = 'virtual.machine.partners'

    vm_id = fields.Many2one('virtual.machine.info',
                            string=_("Amazon Machine Name"))
    info = fields.Text(string=("Información"))
    partner_id = fields.Many2one('res.partner', string=_("Partner"),
                                 domain="[('is_company','=',True)]")
    start_date = fields.Date(string=_("Start Date"))
    state = fields.Selection(string=_("State"), selection=([
                                            ('available', _("Available")),
                                            ('development', _("Development")),
                                            ('production', _("Production")),
                                            ('demo', _("Demo")),
                                            ]))
    ip_address = fields.Char(string=_("IP Address"))
    dns_name = fields.Char(string=_("DNS Name"))
    port = fields.Integer(string=_("Port"))

    _sql_constraints = [
        ('dns_name_uniq',
         'UNIQUE(dns_name)',
         _("DNS Name already exists")),
    ]
