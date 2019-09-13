# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "Stock Move Propose Lot Available In Stock",
    'version': '11.0.1.0.0',
    'author': "François WYAIME @ AbAKUS it-solutions SARL",
    'description': """
When a manufacturing order is going to be produce, only display product lots that are available in stock.
When a stock move is going to be produced, only display product lots that are available in source lcoation.

This module has been developped by François Wyaime @ AbAKUS it-solutions.
    """,
    'license': 'AGPL-3',
    'website': "http://www.abakusitsolutions.eu",
    'depends': [
        'mrp'
    ],
    'category': 'Mrp',
    'data': [
        'wizard/mrp_product_produce.xml',
        'wizard/stock_move_line.xml',
    ],
    'installable': True
}
