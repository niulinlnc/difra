# -*- coding: utf-8 -*-
{
    'name': "Distributor to Customer management",

    'summary': """
        Distributors and final clients stock transfers management """,

    'description': """
        This module allows to set a customer as a distributor or to add a distributor to a partner, making the partner a customer of the
        distributor chosen.

        It creates a new type of operation that will contain the stock transfers between the distributor and his customers.

        This module has been developed by Arbi AMPUKAJEV, intern @ ABAKUS IT-SOLUTIONS.
    """,

    'author': "ABAKUS IT-SOLUTIONS",
    'website': "https://www.abakusitsolutions.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '11.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'sale'
        ],

    # always loaded
    'data': [
        'data/data.xml',
        'views/res_partner_view.xml',
        'views/stock_picking_view.xml',
    ],
}