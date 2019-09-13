# -*- coding: utf-8 -*-
{
    'name': "MRP Show Product contains BOM in used BOM",
    'summary': """MRP Show Product contains BOM in used BOM
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'MRP',
    'version': '11.0.1.1',

    'depends': [
        'mrp',
    ],

    'data': [
        'views/mrp_bom_view.xml',
        'views/mrp_production_view.xml'
    ],

    'installable': True
}