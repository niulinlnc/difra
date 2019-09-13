# (c) AbAKUS IT Solutions
{
    'name': "Purchase flag has photo",
    'version': '11.0.1.0.0',
    'author': "AbAKUS it-solutions SARL",
    'license': 'AGPL-3',
    'summary': "Adds has_photo flag on POL and Picking list",
    'website': "http://www.abakusitsolutions.eu",
    'depends': [
        'stock',
        'purchase'
    ],
    'category': 'Product',
    'data': [
        'views/purchase_views.xml',
        'views/stock_picking_views.xml',
    ],
    'application': False,
    'installable': True,
}
