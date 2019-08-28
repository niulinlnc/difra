# -*- coding: utf-8 -*-
{
    'name': "Difra Price Management",

    'summary': """
    """,

    'description': """
        
        This module has been developed by Valentin Thirion @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION,  AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Base',
    'version': '11.0.1.0',

    'depends': [
        'sale',
        'purchase',
        'purchase_discount',
    ],

    'data': [
        'views/res_product.xml',
        'views/res_partner.xml',
        'views/product_supplierinfo.xml',
    ],
}