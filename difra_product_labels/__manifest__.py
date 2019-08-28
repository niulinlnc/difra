# -*- coding: utf-8 -*-
{
    'name': "DIFRA : Product Labels",

    'summary': """
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'sale',
        'stock',
    ],

    'data': [
        'data/paper_format.xml',

        'views/stock_picking_view.xml',

        'reports/product_label_internal.xml',
        'reports/product_label_external.xml',
    ],
}