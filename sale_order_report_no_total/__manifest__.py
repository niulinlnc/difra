# -*- coding: utf-8 -*-
{
    'name': "Sale Order No Total",
    'summary': """Prints the SO without the total
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'sale',
    ],

    'data': [
        'views/sale_order_view.xml',
        'reports/sale_order_report.xml',
    ],

    'installable': True
}