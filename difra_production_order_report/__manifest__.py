# -*- coding: utf-8 -*-
{
    'name': "DIFRA : Production Order Report",

    'summary': """
    """,
    'description': """
    This module provides improvements to production order report for Difra Company.
    
    
    This module has been developped by François WYAIME, AbAKUS it-solutions PGmbH
    """,
    'author': "François WYAIME, AbAKUS it-solutions PGmbH",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Mrp',
    'version': '11.0.1.0',

    'depends': [
        'mrp',
        'stock',
        'stock_product_usual_location'
    ],

    'data': [
        'reports/production_order_template.xml',
    ],
}