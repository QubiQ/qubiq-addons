# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import _, api, SUPERUSER_ID
import logging


def post_init_hook(cr, registry):

    """
    product_template: copiamos los valores de las traducciones a un campo
    nuevo.
    """
    cr.execute("""
        update ir_translation
        set tra_ant = src
        where name = 'product.template,name' or name = 'product.product,name'
        """)

    """
    product_template: Realizamos el cambio de los nombres traducidos
    para que en todos los idiomas sea el mismo nombre. Se cambia el nombre
    en el producto base y en la bbdd ya que es un campo calculado por defecto
    a la creacion con la primera traduccion encontrada.
    """
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        for product in env['product.template'].search([
            ('name', '!=', ''),
            ('name', '!=', False)
           ]):
            # logging.info("-->>> CAMBIO: " + str(product.id))
            try:
                cr.execute("""
                    select value
                    from ir_translation
                    where name = 'product.template,name' and res_id = %s
                    limit 1
                    """, (product.id,))
                name = cr.fetchall()
                if name:
                    # logging.info("<<- nombre: " + str(name[0][0]))
                    cr.execute("""
                        update product_template
                        set name = %s
                        where id = %s;
                        update ir_translation
                        set src = %s
                        where name = 'product.template,name' and res_id = %s;
                        """, (name[0][0], product.id, name[0][0], product.id))
            except ValueError:
                continue
