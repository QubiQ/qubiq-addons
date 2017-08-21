# -*- coding: utf-8 -*-
# Copyright (c) 2017 QubiQ (http://www.qubiq.es)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    'name': 'Popup notifications mail',
    'version': '8.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Popup de mensajeria',
    'description': '''
    Este modulo ha sido modificado por Qubiq realizar un popup en la descarga y
    asignación de correos de cada usuario.
        * Cada popup se realiza cada 3 minutos.
        * Cada popup es independiente por cada ventana del navegador.
        * Existe un cron que crea las notificaciones llamado: Creacion de
            notificaciones de correo
        * Es necesario y esencial que el parametro de configuracion
            (configuracion->parametros->parametros del sistema) tenga
            la direccion:puerto de la web seguido de /web# por ej:
            http://localhost:8069/web#
        * Para que el popup pase a estado realizado se deberá clicar en "Ok"

    ''',
    'auto_install': False,
    'author': 'Qubiq',
    'website': 'https://www.qubiq.es',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'views/popup_notifications.xml',
            ],
    'qweb': [
        'static/xml/base_popup.xml',
            ],
    'js': [

            ],
    'demo': [

            ],
    'test': [

            ],
    'license': 'AGPL-3',
    #'images': ['static/description/main.png'],
    'update_xml': [],
    'application': True,
    'installable': True,
    'private_category': False,
    'external_dependencies': {
    },

}
