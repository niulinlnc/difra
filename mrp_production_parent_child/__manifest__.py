# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "Mrp Production Parent Child",
    'version': '11.0.1.0',
    'author': "ABAKUS it-solutions GmbH",
    'description': """
This module adds fields to model mrp.production to bring productions and sub-productions together.
It also adds a comment fields that is copied from parent production to all child productions.

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
