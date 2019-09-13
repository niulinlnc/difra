# -*- coding: utf-8 -*-
{
    'name': "MRP Scheduler Launch Menuitems",

    'summary': """
    """,

    'description': """
        MRP Scheduler Launch Menuitems
        
        This module adds menuitems in sale, purchase and manufacture apps to allow users to run scheduler manually.
        
        This module has been developed by AbAKUS it-solutions.
    """,

    'author': "AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Manufacturing',
    'version': '11.0.1.0',

    'depends': [
        'mrp',
        'stock'
    ],

    'data': [
        'views/sale.xml',
        'views/purchase.xml',
        'views/mrp.xml',
    ],

    'installable': True
}
