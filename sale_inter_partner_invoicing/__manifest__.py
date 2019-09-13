# -*- coding: utf-8 -*-
{
    'name': "Sale Inter-Partner Invoicing",

    'summary': """
    """,

    'description': """
        Sale Inter-Partner Invoicing

        This module adds a field many2many on the partner form to allow create inter-partner links.

        These links will be used to allow an invoicing splitting when creating the invoices (using a pop-up window).
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '10.0.1.0',

    'depends': [
        'base',
        'sale',
        'account',
    ],

    'data': [
        'views/res_partner_view.xml'
    ],
}