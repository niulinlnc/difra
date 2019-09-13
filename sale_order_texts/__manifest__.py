# -*- coding: utf-8 -*-
{
    'name': "Sale Order Texts",
    'summary': """Add header and footer texts in SO
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.1',

    'depends': [
        'sale',
        'account_invoice_text',
        'stock_picking_list_text',
    ],

    'data': [
        'views/sale_order_view.xml',
        'reports/sale_order_report.xml',
    ],

    'installable': True
}