# -*- coding: utf-8 -*-
{
    'name': "Product Suppliers Edit Restrict to Non Managers",

    'summary': """
    """,

    'description': """
        Product Suppliers Edit Restrict to Non Managers

        This modules makes the supplier list of the products non editable for non Purchase-Managers.
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Purchase',
    'version': '10.0.1.0',

    'depends': [
        'purchase',
        'sale'
    ],

    'data': [
        'views/product_template.xml',
    ],
}