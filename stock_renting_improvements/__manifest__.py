# -*- coding: utf-8 -*-
{
    'name': "Stock Renting Improvements",

    'summary': """
    """,
    'description': """
Stock Renting Improvements    

This module adds specific information to stock picking document related to renting and loan management.\r\n
-> Adds a selection field to specify if stock picking concerns a renting or a loan.\r\n
-> Adds a char field to specify delivery mode.\r\n
-> Adds a note field to add comment to the stock picking.\r\n 

This module has been developped by François Wyaime @ AbAKUS it-solutions.
    """,
    'author': "François WYAIME, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Stock',
    'version': '11.0.1.0',

    'depends': [
        'stock',
        'difra_delivery_slip_report',
    ],

    'data': [
        'views/stock_picking_type.xml',
        'views/stock_picking.xml',

        'reports/delivery_slip_template.xml'
    ],

    'installable': True
}
