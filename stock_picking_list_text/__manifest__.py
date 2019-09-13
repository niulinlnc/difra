# -*- coding: utf-8 -*-
{
    'name': "Stock Picking Texts",
    'summary': """Add header and footer texts in Picking Lists  
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Stock',
    'version': '11.0.1.1',

    'depends': [
        'purchase',
    ],

    'data': [
        'views/stock_picking_view.xml',
        'reports/stock_picking_report.xml',
    ],

    'installable': True
}