# -*- coding: utf-8 -*-
{
    'name': "MRP Expand Sub-BoM in current BoM",
    'summary': """MRP Expand Sub-BoM in current BoM
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'MRP',
    'version': '11.0.1.1',

    'depends': [
        'mrp_bom_product_composed',
    ],

    'data': [
        'views/mrp_bom_view.xml',
    ],

    'installable': True
}