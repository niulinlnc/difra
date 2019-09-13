# -*- coding: utf-8 -*-
{
    'name': "Partner Customer State",

    'summary': """
    """,

    'description': """
        Partner Customer State
        
        Adds prospect/customer/ex-customer state to partner if it is a 'customer'.
        
        This module has been developed by Jason PINDAT, intern @ AbAKUS it-solutions.
    """,

    'author': "Jason PINDAT, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '10.0.1.0',

    'depends': ['base', 'sale'],

    'data': [
        'views/res_partner.xml'
    ],
}