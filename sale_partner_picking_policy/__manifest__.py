# -*- coding: utf-8 -*-
{
    'name': "Picking Policy on Partner",
    'summary': """Add a picking policy selection on partner and use it on SO
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.1',

    'depends': [
        'sale_stock',
    ],

    'data': [
        'views/res_partner_view.xml',
    ],

    'installable': True
}