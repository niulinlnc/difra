# -*- coding: utf-8 -*-
{
    'name': "Product Cost History",

    'summary': """
    """,

    'description': """
        Product Cost History
        
        Adds cost history to products, an history line is added when a purchase is confirmed
        
        This module has been developed by Jason PINDAT, intern @ AbAKUS it-solutions.
    """,

    'author': "Jason PINDAT, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Product',
    'version': '11.0.1.0',

    'depends': [
        'base',
        'purchase'
    ],

    'data': [
        'views/product_template.xml',
        'views/product_cost_history.xml',
        'security/ir.model.access.csv'
    ],
}