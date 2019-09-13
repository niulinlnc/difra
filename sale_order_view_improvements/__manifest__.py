# -*- coding: utf-8 -*-
{
    'name': "Sale Order View Improvements",

    'summary': """
    """,

    'description': """
Sale Order View improvement\n
\n      
This module adds improvements to the sale.order tree view and to the sale.order form view:\n
        
-> Adds a boolean to form view: True if products are delivered, else otherwise.\n
-> Adds a boolean to tree view: True if products are delivered, else otherwise.\n
-> Adds client order reference to  tree view (field client_order_ref).\n
\n        
This module has been developed by François WYAIME @ AbAKUS it-solutions.
    """,

    'author': "François WYAIME, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'sale'
    ],

    'data': [
        'views/sale_order.xml',
    ],

    'installable': True
}
