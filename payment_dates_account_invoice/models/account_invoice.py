# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api
from datetime import datetime, timedelta,date,time



class account_invoice(models.Model):
    _inherit = 'account.invoice'

    due_dates_str = fields.Char(string="Due dates",compute='_get_due_dates_str')

    def _get_due_dates(self):
        if (self.date_invoice) :
            pterm = self.env['account.payment.term'].browse(self.payment_term.id)
            pterm_list = pterm.compute(value=self.amount_total,date_ref=self.date_invoice)
            final_list=[]
            if (pterm_list[0]) :
                for line in pterm_list[0] :
                	d=datetime.strptime(line[0], '%Y-%m-%d')        	
                	final_list.append((datetime.strftime(d, "%d/%m/%Y"),str(line[1]),self.currency_id.symbol), )
               
                return final_list
            
        else :
            return ''
        
 
    def _get_due_dates_str(self):
        if (self.date_invoice) :



            pterm = self.env['account.payment.term'].browse(self.payment_term.id)

            pterm_list = pterm.compute(value=self.amount_total,date_ref=self.date_invoice)
            final_str=""
            if (pterm_list[0]) :
                for line in pterm_list[0] :
                    d=datetime.strptime(line[0], '%Y-%m-%d')                        
                    final_str=final_str+' '+(datetime.strftime(d, "%d/%m/%Y"))
           
            self.due_dates_str=final_str
        else :
            self.due_dates_str=False




        
    
    

