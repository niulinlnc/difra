# -*- coding: utf-8 -*-
{
    'name': "Stock 'Usual Location' info on Products and Stock Reports",

    'summary': """
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Stock',
    'version': '11.0.1.0',

    'depends': [
        'stock',
    ],

    'data': [
        'views/product_view.xml',
        'reports/picking_list_report.xml',
        'reports/stock_inventory_report.xml',
    ],

    'installable': True
}
