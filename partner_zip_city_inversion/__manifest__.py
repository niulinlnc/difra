# -*- coding: utf-8 -*-
{
    'name': "Partner ZIP & City Inversion",

    'summary': """
    """,

    'description': """
        Partner ZIP & City Inversion

        Out of the box, Odoo presents the address fields as:
        Street 1
        Street 2
        City / State / ZIP
        Country

        This modules changes it to:
        Street 1
        Street 2
        ZIP / State / City
        Country
        
        This module has been developed by AbAKUS it-solutions.
    """,

    'author': "AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'base',
    ],

    'data': [
        'views/res_partner_view.xml',
    ],

    'installable': True
}
