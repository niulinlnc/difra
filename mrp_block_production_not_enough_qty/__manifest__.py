# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "Mrp Block Production Not Enough Quantity",
    'version': '11.0.1.0',
    'author': "AbAKUS it-solutions SARL",
    'description': """
If there is not enough quantity in a production to be produced, the user will not be able to produce it thanks to this module. 
The module also triggers a warning if any of qty_done are not filled when recording production.

This module has been developped by François Wyaime @ ABAKUS it-solutions GmbH.
    """,
    'license': 'AGPL-3',
    'website': "http://www.abakusitsolutions.eu",
    'depends': [
        'mrp'
    ],
    'category': 'Mrp',
    'data': [
        'views/mrp_production.xml'
    ],
    'installable': True
}
