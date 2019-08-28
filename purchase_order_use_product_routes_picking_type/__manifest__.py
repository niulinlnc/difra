# (c) AbAKUS IT Solutions
{
    'name': "Purchase Order Use Product Routes Picking Type",
    'version': '11.0.1.0',
    'author': "François WYAIME @ AbAKUS it-solutions SARL",
    'license': 'AGPL-3',
    'description': """
Purchase Order Use Product Routes Picking Type
    
This module is useful when you have more than one picking type operation for buying products.

This is an example with 2 different types: type 1 and type 2.
If you want to buy 1 product which has type 1 and one product which has type 2 but both have the same supplier, without this module you have to do 2 purchase orders and specify in both purchase order which type you want to use.

This module won't take into account the type of the purchase order but the type of each product defined as order_line in the purchase order.
It means that you can create only one purchase order with products that have different types, but the supplier must be the same for each product.
 
This module has been developped by François Wyaime @ AbAKUS it-solutions.
    """,
    'website': "http://www.abakusitsolutions.eu",
    'depends': [
        'purchase'
    ],
    'category': 'Purchase',
    'data': [
        'views/purchase_order_view.xml',
    ],
    'application': False,
    'installable': True,
}
