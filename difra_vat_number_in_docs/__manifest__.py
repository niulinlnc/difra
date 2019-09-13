# -*- coding: utf-8 -*-
{
    'name': "DIFRA VAT Number in docs",

    'summary': """
    """,

    'description': """
Difra VAT Number in docs

This module adds a vat Char field (related to the partner of the linked doc) in:
- SO
- PO
- Invoice
- PL
    
This module has been developed by Valentin Thirion @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION,  AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Base',
    'version': '11.0.1.0',

    'depends': [
        'sale',
        'purchase',
        'stock',
        'account',
    ],

    'data': [
        'views/sale_order_view.xml',
        'views/picking_list_view.xml',
        'views/purchase_order_view.xml',
        'views/account_invoice_view.xml',
    ],
}