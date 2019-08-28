# -*- coding: utf-8 -*-
{
    'name': "Sale Order Invoice Method based on Partner",

    'summary': """
    """,

    'description': """
        Sale Order Invoice Method based on Partner

        This modules adds a selection field on partner for the invoicing method:
        - invoice for every sale order
        - invoice every month
        - invoice for every delivery
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '10.0.1.0',

    'depends': [
        'sale',
        'account'
    ],

    'data': [
        'views/partner.xml',
        'views/sale_order.xml',
    ],

    'installable': True
}
