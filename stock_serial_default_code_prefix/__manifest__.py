# -*- coding: utf-8 -*-
{
    'name': "Stock Serial Default Code Prefix",

    'summary': """
    """,

    'description': """
        Stock Serial Default Code Prefix
        
        This module override create method on stock.production.lot to prefix sequence with default code.
        
        This module has been developed by ABAKUS IT-SOLUTIONS.
    """,

    'author': "ABAKUS IT-SOLUTIONS",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Stock',
    'version': '1.0.1.0',

    'depends': [
        'base',
        'mrp',
        'stock'
    ],

    'data': [
    ],

    'installable': True
}
