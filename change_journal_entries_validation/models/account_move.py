# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)

from openerp import api, models, _
from openerp.exceptions import UserError


class account_move(models.Model):
    _inherit = 'account.move'

    """
    Se hereda la funcion para realizar el chequeo de que los
    asientos al postearlo debido a que se quita esta funcionalidad
    cuando se hace el write por la herencia de la funcion assert_balanced
    """
    @api.multi
    def post(self):
        for move in self:
            move.assert_balanced(force=True)
        return super(account_move, self).post()

    """
    Se sobreescribe esta funcion debido a que si no,
    no es posible el cambio de los importes.
    """
    @api.multi
    def assert_balanced(self, force=False):
        if self.state != 'draft' or force:
            if not self.ids:
                return True
            prec = self.env['decimal.precision'].precision_get('Account')

            self._cr.execute("""\
                SELECT      move_id
                FROM        account_move_line
                WHERE       move_id in %s
                GROUP BY    move_id
                HAVING      abs(sum(debit) - sum(credit)) > %s
                """, (tuple(self.ids), 10 ** (-max(5, prec))))
            if len(self._cr.fetchall()) != 0:
                raise UserError(_("Cannot create unbalanced journal entry."))
        return True
