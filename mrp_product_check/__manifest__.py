# -*- coding: utf-8 -*-
{
    'name': "Product Check in BOM",

    'summary': """
    """,

    'description': """
        Product Check in BOM
        
        This modules uses ``product_check`` (AbAKUS it-solutions's sale repo) to clearly tell the user that the product used in the BOM is not checked.
        
        This module has been developed by AbAKUS it-solutions.
    """,

    'author': "AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Manufacturing',
    'version': '11.0.1.0',

    'depends': [
        'product_check',
        'mrp',
    ],

    'data': [
        'views/mrp_bom_view.xml',
    ],

    'installable': True
}
