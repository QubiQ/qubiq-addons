from openerp import models, fields, exceptions, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning



class account_invoice(models.Model):
	_inherit = "account.invoice"

	@api.multi
	def nif_validate(self):
		if self.partner_id.vat:			
			self.signal_workflow('invoice_open')
				
		else:
			raise Warning(_("The partner needs a valid TIN."))