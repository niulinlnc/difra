# -*- coding: utf-8 -*-
{
    'name': "Sale Order Line Invoice and Shipping Partner",
    'summary': """Sale Order Line Invoice and Shipping Partner
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'sale',
        'account',
        'sale_stock',
    ],

    'data': [
        'views/product_view.xml',
    ],

    'installable': True
}