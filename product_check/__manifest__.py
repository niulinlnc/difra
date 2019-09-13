# -*- coding: utf-8 -*-
{
    'name': "Product Check",

    'summary': """
    """,

    'description': """
        Product Check
        
        Adds 'Checked' option to product.template
        If a product is not checked, it will show it clearly when using it in a Sale Order Line.
        
        This module has been developed by Jason PINDAT, intern @ AbAKUS it-solutions.
    """,

    'author': "AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'sale',
    ],

    'data': [
        'views/product.xml',
        'views/sale_order_line_view.xml',
    ],

    'installable': True
}
