# -*- coding: utf-8 -*-
{
    'name': "Difra Default Order Tree View",

    'summary': """
    """,

    'description': """
        This modules adds default order attributes for spécific tree views:\n
        \n
        -> Stock Pickings
        -> Stock Move\n
        
        This module has been developed by François Wyaime @ AbAKUS it-solutions.
    """,

    'author': "François WYAIME, AbAKUS it-solutions GmbH",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'base',
    'version': '11.0.1.0',

    'depends': [
        'stock'
    ],

    'data': [
        'views/stock_picking.xml',
        'views/stock_move_line.xml'
    ],
}