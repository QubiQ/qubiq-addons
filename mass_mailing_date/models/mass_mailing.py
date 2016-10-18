# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
import datetime

class MassMailing(models.Model):
	_inherit = 'mail.mass_mailing'

	bool_for_send = fields.Boolean(string='Ready to send',default=False)
	date_for_send_mail = fields.Date(string='Date to send')


	@api.model
	def _cron_envio_mails_masivos(self):
		mail_objs = self.env['mail.mass_mailing'].search([
											                ('bool_for_send', '=', True),           
											                ('sent_date','=',False),
											                ('date_for_send_mail','!=',False),
											                ('date_for_send_mail','=',datetime.date.today())
											            ])
		for mail_obj in mail_objs:
			mail_obj.send_mail()