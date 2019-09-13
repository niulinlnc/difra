# -*- coding: utf-8 -*-
{
    'name': "Partners for Pricelist",

    'summary': """
    """,

    'description': """
        Partners for Pricelist

        Adds a button in the pricelist to show the partners linked to this PL.
        
        This module has been developed by @ AbAKUS it-solutions.
    """,

    'author': "AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'sale',
    ],

    'data': [
        'views/product_pricelist.xml',
        'views/res_partner.xml',
    ],

    'installable': True
}
