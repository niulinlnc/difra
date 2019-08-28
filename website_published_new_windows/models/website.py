from odoo import api, fields, models, tools

class WebsitePublishedMixinNewPage(models.AbstractModel):

    _inherit = "website.published.mixin"

    def open_website_url(self):
        return {
            'type': 'ir.actions.act_url',
            'url': self.website_url,
            'target': '_blank',
        }