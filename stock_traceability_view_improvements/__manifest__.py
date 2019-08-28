# -*- coding: utf-8 -*-
{
    'name': "Stock Traceability View Improvements",

    'summary': """
    """,
    'description': """
    Stock Traceability View Improvements
    
    This module adds view improvements 
    """,

    'author': "François WYAIME, AbAKUS it-solutions PGmbH",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Stock',
    'version': '11.0.1.0',

    'depends': [
        'stock',
    ],

    'data': [
        'views/stock_quant.xml',
        'views/stock_move_line.xml'
    ],

    'installable': True
}
