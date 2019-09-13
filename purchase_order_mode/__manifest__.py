# (c) AbAKUS IT Solutions
{
    'name': "Purchase order mode",
    'version': '11.0.1.0.0',
    'author': "AbAKUS it-solutions SARL",
    'license': 'AGPL-3',
    'summary': "Adds purchase_mode selector on purchase order",
    'website': "http://www.abakusitsolutions.eu",
    'depends': [
        'purchase'
    ],
    'category': 'Purchase',
    'data': [
        'views/partner_view.xml',
        'views/purchase_views.xml',
    ],
    'application': False,
    'installable': True,
}
