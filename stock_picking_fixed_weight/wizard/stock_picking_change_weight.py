# -*- coding: utf-8 -*-


from openerp import models, fields, api


class stock_picking_change_weight(models.TransientModel):
    """Import Confirmation"""
    _name = "stock.picking.change.weight"

    weight=fields.Float(string="New weight")


    @api.one
    def confirm(self):

    	act_close = {'type': 'ir.actions.act_window_close'}
        packs_ids = self._context.get('active_ids')
        if packs_ids is None:
            return act_close
        assert len(packs_ids) == 1, "Only 1 picking ID expected"
        pack = self.env['stock.picking'].browse(packs_ids)
        pack.weight_fixed=self.weight        
       

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
