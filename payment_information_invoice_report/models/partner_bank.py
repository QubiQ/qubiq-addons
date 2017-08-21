from openerp import models, fields, api

class res_partner_bank(models.Model):
	_inherit = 'res.partner.bank'
	secret_acc = fields.Char(string='Available',compute='_get_secret_number',store=False)

	@api.multi
	def _get_secret_number(self):
		for s in self :
			if s.acc_number:
				s.secret_acc = "****************"+s.acc_number[-4:]
			else :
				s.secret_acc = ""

