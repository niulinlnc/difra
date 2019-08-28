# -*- coding: utf-8 -*-
{
    'name': "Search for product by description",
    'summary': """
    """,

    'description': """
        Search for product by description
        
        Adds 'Description' in the search criterias and looks for all description fields in a product
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'purchase',
        'stock',
        'sale'
    ],

    'data': [
        'views/product_search.xml',
    ],

    'installable': True
}
