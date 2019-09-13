# -*- coding: utf-8 -*-
{
    'name': "Product hide sale price",

    'summary': """
        Hides the sale price of the products 'everywhere'
    """,

    'description': """
        Product hide sale price

        This module hides the sale price of the products 'everywhere'
        Views : form, list and kanban

        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'version': '10.0.1.0',
    'depends': [
        'product'
    ],
    'data': [
        'views/product_view.xml',
    ],
    
    'installable': True
}