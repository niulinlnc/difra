# -*- coding: utf-8 -*-
{
    'name': "Partner note in Sale Order Form",

    'summary': """
    """,

    'description': """
        Partner note in Sale Order Form

        This modules adds a new field 'sale order comment' in the partner and shows it in the sale order form in a very viewable way.
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '10.0.1.0',

    'depends': [
        'sale',
    ],

    'data': [
        'views/sale_order.xml',
    ],

    'installable': True
}
