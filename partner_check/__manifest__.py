# -*- coding: utf-8 -*-
{
    'name': "Partner Check",

    'summary': """
    """,

    'description': """
        Partner Check
        
        Adds
        - 'Checked' option to res.partner
        - If a 'non-checked' partner is associated to a  Sale Order, it displays a warning message
        
        This module has been developed by Jason PINDAT & Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Jason PINDAT, Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'base',
        'sale',
    ],

    'data': [
        'views/partner.xml',
        'views/sale_order.xml',
    ],

    'installable': True
}
