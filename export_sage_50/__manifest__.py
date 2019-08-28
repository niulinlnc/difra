# -*- encoding: utf-8 -*-
# Subject to license. See LICENSE file for full copyright and licensing details.
{
    'name': 'Export Sage BOB 50',
    'version': '9.0.1.0',
    'author': 'be-Cloud.be (Jerome Sonnet), AbAKUS it-solutions (Valentin Thirion, Jason Pindat)',
    'website': '',
    'category': 'Accounting',
    'depends': [
        'account_accountant',
        'l10n_be',
        'analytic',
    ],
    'data': [
        'views/export_sage_50.xml',
        'views/account_tax.xml',
        'views/account_fiscal_position.xml',
        'views/account_sage_code.xml',
        'views/account_analytic_account.xml',
        'views/res_company.xml',
        'views/menu_buttons.xml',

        'data/sage_codes.xml',
        'data/ir_rule.xml',

        'security/ir.model.access.csv',
    ],
    'description': '''
        Export Sage 50

        This modules creates an export of compatible invoices with Sage BOB 50.

        Configuration needed:
            - Sage 50 tax codes in Accounting => Configuration => Taxes
            - Fiscal Position Sage 50 statuses Accounting => Configuration => Fiscal Position
    ''',
    'installable': True,
    'application': False,
}
