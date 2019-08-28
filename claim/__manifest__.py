# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "Claim App",
    'version': '11.0.1.0.0',
    'author': "François WYAIME @ AbAKUS it-solutions SARL",
    'description': """
This app add a claim system to manage After Sale Service, claim and repair management.

This module has been developped by François Wyaime @ AbAKUS it-solutions.
    """,
    'license': 'AGPL-3',
    'website': "http://www.abakusitsolutions.eu",
    'depends': [
        'mrp',
        'mrp_repair',
        'mail',
        'calendar',
        'calendar_sms'
    ],
    'category': 'Claim',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/ir_sequence.xml',
        'data/stock_picking_type.xml',

        'views/claim_app.xml',
        'views/claim.xml',
        'views/claim_as_team.xml',
        'views/claim_tag.xml',
        'views/stock_picking.xml',
        'views/mrp_repair_default_test.xml',
        'views/mrp_repair.xml',
        'views/calendar_event.xml',

        'report/mail_templates.xml',
        'report/claim_report.xml',
        'report/mrp_repair_report.xml',
    ],
    'installable': True,
    'application': True
}
