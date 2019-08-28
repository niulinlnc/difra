# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "Stock Move Register End of Life Date",
    'version': '11.0.1.0',
    'author': "François WYAIME @ AbAKUS it-solutions SARL",
    'description': """
This module allows user to fill an end of life date when they are encoding lot/serial numbers.

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
