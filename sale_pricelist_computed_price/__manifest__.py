# -*- coding: utf-8 -*-
{
    'name': "Sale Pricelist Computed Price",

    'summary': """
    """,

    'description': """
        Sale Pricelist Computed Price

        This module adds a computed field in the pricelist lines related to a single product that will contains the computed price for this product and this line.

        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '10.0.1.0',

    'depends': [
        'sale',
    ],

    'data': [
        'views/pricelist_view.xml'
    ],
}