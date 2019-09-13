# -*- coding: utf-8 -*-
{
    'name': "Sale Order Template",

    'summary': """
    """,

    'description': """
        Sale Order Template
        
        Adds a sale orders templating system.
        Some fields (for example the taxes management) couldn't be integrated (depending on the customer)
        
        This module has been developed by Jason PINDAT, intern @ AbAKUS it-solutions.
    """,

    'author': "Jason PINDAT, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '10.0.1.0',

    'depends': ['base', 'sale'],

    'data': [
        'views/sale_order_template.xml',
        'views/sale_order.xml',
        'views/menu_button.xml',
        'security/ir.model.access.csv'
    ],
}