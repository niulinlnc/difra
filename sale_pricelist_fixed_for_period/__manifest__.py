# -*- coding: utf-8 -*-
{
    'name': "Sale Pricelist Fixed for Period and Product list",

    'summary': """
    """,

    'description': """
        Sale Pricelist Fixed for Period and Product list

        - select some products
        - set the way you want to fix prices
        - generate fixed prices lines in this pricelist

        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'base',
        'product',
        'sale'
    ],

    'data': [
        'views/pricelist_view.xml',
        'views/product_view.xml',

        'security/ir.model.access.csv',
    ],
}