# -*- coding: utf-8 -*-
# Copyright 2014-2015  Grupo ESOC <www.grupoesoc.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Disable partner creation",
    "version": "11.0.1.0",
    "author": "AbAKUS it-solutions",
    "category": "Sale",
    "website": "https://www.abakusitsolutions.eu",
    "depends": [
        "account",
        "sale",
        "stock",
        "purchase",
    ],
    "data": [
        "views/account_forms.xml",
        "views/sale_forms.xml",
        "views/stock_forms.xml",
        "views/purchase_forms.xml",
    ],
    'installable': True,
}
