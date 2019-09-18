==================================
Stock Serial Default Code Prefix
==================================

This module override create method on stock.production.lot to prefix sequence with default code.

Configuration
=============

- Install the module through Apps module.
- Go to Settings > Technical > Sequence and find stock.lot.serial sequence.
- Configure it with following parameters:

    -   Implementation: Standard
    -   Prefix: %(y)s
    -   Sequence Size: 5
    -   Step: 1
    -   Sequence Code: stock.lot.serial

Author
======

* Francois Wyaime <francois.wyaime@abakusitsolutions.eu>

Maintainer
-----------

.. image:: http://www.abakusitsolutions.eu/wp-content/themes/abakus/images/logo.gif
   :alt: ABAKUS IT-SOLUTIONS
   :target: http://www.abakusitsolutions.eu

This module is maintained by ABAKUS IT-SOLUTIONS

