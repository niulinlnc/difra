# -*- coding: utf-8 -*-
{
    'name': "Salesmen for Contacts",

    'summary': """
    """,

    'description': """
        This module sets every new contact with the salesmen as the current user.

        It also shows the salesmen field in the mini-contact form view.
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '10.0.1.0',

    'depends': [
        'base',
        'sale'
    ],

    'data': [
        'views/res_partner_view.xml'
    ],
}