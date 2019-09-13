# -*- coding: utf-8 -*-
{
    'name': "Difra Product Purchase Price Checker",
    'description': """
    This module checks if the purchase price of each product is the same as last price history.
    
    This module has been developped by AbAKUS it-solutions.""",
    'author': "François Wyaime, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'version': '11.0.1.1',

    'depends': [
        'sale',
    ],

    'data': [
        'views/product_check_purchase_price_view.xml'
    ],
    'installable': True
}