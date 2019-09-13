# (c) AbAKUS IT Solutions
{
    'name': "Sale Order Line Description in Move Line",
    'version': '11.0.1.0.0',
    'author': "AbAKUS it-solutions SARL",
    'license': 'AGPL-3',
    'summary': "Display SOL description in corresponding PL",
    'depends': [
        'stock',
    ],
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sales',
    'data': [
        'views/stock_picking_views.xml',
    ],
    'application': False,
    'installable': True,
}
