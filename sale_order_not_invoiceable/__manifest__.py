# -*- coding: utf-8 -*-
{
    'name': "Sale Order Not Invoiceable",

    'summary': """
    """,

    'description': """
Sale Order Not Invoiceable\n
\n      
This modules adds a checkbox to the sale order form. \n
If true, the button to create invoice is disabled, otherwise, the button to create invoice is enabled.\n
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
