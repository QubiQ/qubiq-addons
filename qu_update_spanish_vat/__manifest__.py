# -*- coding: utf-8 -*-
# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Qu Update Spanish VAT",
    "summary": "Adds ES ahead spanish customers's VAT",
    "version": "10.0.1.0.0",
    "category": "Custom",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "depends": [
        "base",
    ],
    "data": [
        "data/scheduled_action.xml",
        "views/res_partner.xml"
    ],
    "application": False,
    "installable": True,
}
