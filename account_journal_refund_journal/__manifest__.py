# -*- coding: utf-8 -*-
{
    'name': "Account Journal Refund Journal",
    'summary': """Use another journal for refunds
    """,
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Account',
    'version': '11.0.1.1',

    'depends': [
        'purchase',
    ],

    'data': [
        'views/account_journal_view.xml',
    ],

    'installable': True
}