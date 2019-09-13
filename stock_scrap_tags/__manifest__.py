# -*- coding: utf-8 -*-
{
    'name': "Stock Scrap Tags",

    'summary': """
    """,
    'description': """
    This module adds tags in stock scrap, this tags allows to filter scraps and to know why they are in scrap location.\n
    It adds a menuitem in inventory configuration to allow only inventory manager to manage tags. This avoid all users to create tags.\n\n
    
    This module has been developped by François Wyaime @ AbAKUS it-solutions.
    """,

    'author': "François WYAIME, ABAKUS IT-SOLUTIONS GmbH",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Stock',
    'version': '11.0.1.0',

    'depends': [
        'stock',
    ],

    'data': [
        'views/stock_scrap.xml',
        'views/stock_scrap_tag.xml'
    ],

    'installable': True
}
