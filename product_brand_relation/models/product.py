# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
# See LICENSE file for full copyright and licensing details.


from openerp import fields, models

class product_template(models.Model):
    _inherit = "product.template"
        
    brand_id = fields.Many2one(related='product_brand_id', string='Brand')
    
    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        if context is None:
            context = {}
        if 'search_default_brand_id' in context and context.get('search_default_brand_id'):
            args.append(['brand_id','in',context.get('search_default_brand_id')])
        return super(product_template, self).search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count)