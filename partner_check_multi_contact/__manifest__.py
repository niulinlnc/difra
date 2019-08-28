# -*- coding: utf-8 -*-
{
    'name': "Partner Check in Multi-Contact",

    'summary': """
    """,
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Sale',
    'version': '11.0.1.0',

    'depends': [
        'partner_check',
        'partner_contact_in_several_companies',
    ],

    'data': [
        'views/res_partner_view.xml',
    ],

    'installable': True
}
