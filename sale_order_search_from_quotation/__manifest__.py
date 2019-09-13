# -*- coding: utf-8 -*-
{
    'name': "Sale Order Search From Quotation",

    'summary': """
    """,

    'description': """
Sale Order Search From Quotation\n
\n      
This module adds a search criteria in sale.order based on quotation number.
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
