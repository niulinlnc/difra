# -*- coding: utf-8 -*-
{
    'name': "Purchase Supplier Products Restrict",
    'description': """
        Purchase Supplier Products Restrict

    - Restricts the product list display to the products a vendor sells
    - Adds a button in partner view to display the products he sells

    This module has been developped by Jason PINDA, intern @ AbAKUS it-solutions
    """,

    'author': "Jason Pindat, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Uncategorized',
    'version': '1.0.1.0',

    'depends': [
        'base',
        'purchase',
        'product'
    ],

    'data': [
        'views/products_restrict.xml',
        'views/vendor_button.xml',
    ],
}