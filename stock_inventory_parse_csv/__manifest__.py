# -*- coding: utf-8 -*-
{
    'name': "Stock Inventory Parse CSV",
    'summary': """
    """,

    'description': """
        Stock Inventory Parse CSV
        
        This modules adds a text field and a button in stock.inventory form to parse csv and fill stock.inventory.line. 
        
        This module has been developed by François WYAIME @ AbAKUS it-solutions.
    """,

    'author': "François WYAIME, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Warehouse',
    'version': '11.0.1.0',

    'depends': [
        'stock',
    ],

    'data': [
        'views/stock_inventory.xml'
    ],

    'installable': True
}
