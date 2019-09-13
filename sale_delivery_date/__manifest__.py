# -*- coding: utf-8 -*-
{
    'name': "Sale Delivery Date",

    'summary': """
    """,

    'description': """
        This module adds a field "delivery date" in the Sales Order to be set manually by the operational person as not using the Warehouse App.
        
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
        'views/sale_order.xml'
    ],
}