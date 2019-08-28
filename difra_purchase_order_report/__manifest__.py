# -*- coding: utf-8 -*-
{
    'name': "DIFRA : Purchase Order Report",

    'summary': """
    """,

    'author': "François WYAIME, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Purchase',
    'version': '11.0.1.0',

    'depends': [
        'purchase',
        'purchase_order_external_reference'
    ],

    'data': [
        'reports/purchase_order_template.xml',
    ],
}