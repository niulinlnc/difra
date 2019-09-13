# -*- coding: utf-8 -*-
{
    'name': "Product Internal Code Non-editable",

    'summary': """
        Set the default_code field non-editable
    """,

    'description': """
        Product Internal Code Non-editable

        This module sets the field 'default_code' non editable in the product view.

        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale',
    'version': '10.0.1.0',
    'depends': [
        'product'
    ],
    'data': [
        'views/product_view.xml',
    ],
    
    'installable': True
}