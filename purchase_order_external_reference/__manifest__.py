# -*- coding: utf-8 -*-
{
    'name': "Purchase Order External Reference",

    'summary': """
    """,

    'description': """
        Purchase Order External Reference

        This module adds a the partner external reference in the PO and in the report associated.
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valent THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Product',
    'version': '10.0.1.0',

    'depends': [
        'base',
        'purchase',
        'partner_reference_external',
    ],

    'data': [
        'views/purchase_order.xml',
        'reports/purchase_order_reports.xml',
    ],
}