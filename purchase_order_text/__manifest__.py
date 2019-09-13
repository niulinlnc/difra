# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Texts",
    'summary': """Add header and footer texts in PO
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Purchase',
    'version': '11.0.1.1',

    'depends': [
        'purchase',
    ],

    'data': [
        'views/purchase_order_view.xml',
        'reports/purchase_order_report.xml',
    ],

    'installable': True
}