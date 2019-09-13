# -*- coding: utf-8 -*-
{
    'name': "Difra Worker Rights",

    'summary': """
    """,

    'description': """
        This modules adds limitations in product_template_form to hide some fields to workers.
        
        -> Hide price in product_template kanban view
        -> Hide price in product_template tree view
        -> Hide price in tab general informations from product form
        -> Hide invoicing tab from product form
        
        This module has been developed by François Wyaime @ AbAKUS it-solutions.
    """,

    'author': "François WYAIME, AbAKUS it-solutions GmbH",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'security',
    'version': '11.0.1.0',

    'depends': [
        'product',
        'account'
    ],

    'data': [
        'views/product_template.xml',
    ],
}