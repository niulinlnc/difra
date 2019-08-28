# -*- coding: utf-8 -*-
{
    'name': "Sale Pricelist Margin",

    'summary': """
    """,

    'description': """
        Sale Pricelist Margin

        This module adds a price computation mode in the pricelist items settings : margin.

        You can then enter a percentage that will be applied on either the cost or the sale price set on the product.

        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '10.0.1.0',

    'depends': [
        'base',
        'product',
        'sale'
    ],

    'data': [
        'views/pricelist_view.xml'
    ],
}