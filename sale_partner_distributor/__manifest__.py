# -*- coding: utf-8 -*-
{
    'name': "sale_partner_distributor",

    'summary': """
        Distributor and final client stock transfert management """,

    'description': """
        This module allow to set a customer as a distributor or to add a distributor to a partner making the partner a client of the
        distributor chosen.

        It creates a new type of operations that will contain the stock transferts between the distributor and his client.

        This module has been developed by Arbi AMPUKAJEV, intern @ AbAKUS it-solutions, under the control of Valentin Thirion.
    """,

    'author': "Arbi AMPUKAJEV, AbAKUS it-solutions SARL",
    'website': "https://www.abakusitsolutions.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/partner.xml',
        'views/stock-picking.xml',
    ],
}