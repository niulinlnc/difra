# -*- coding: utf-8 -*-
{
    'name': "Stock Tracability Helper",

    'summary': """
    """,

    'description': """
        Stock Tracability Helper
        

        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Stock',
    'version': '1.0.1.0',

    'depends': [
        'base',
        'stock',
    ],

    'data': [
        'wizard/stock_serial_lot_trace_wizard_view.xml',
        'views/stock_tracability_menu.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True
}
