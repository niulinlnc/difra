from odoo import models, fields, api, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    header_text = fields.Text(string="Optional header text")
    footer_text = fields.Text(string="Optional footer text", default=_("Our user manuals are delivered in english. Your acceptance of this quotation expresses your agreement.<br />Nos manuels sont fournis en anglais. Votre acceptation de la présente offre de prix exprime votre accord.<br />Onze handleidingen zijn in het engels geleverd. Uw aanvaarding van deze prijsofferte drukt uw instemming uit.<br />Unsere Gebrauchsanleitungen werden in Englischer Sprache geliefert. Ihre Annahme dieses Angebots drückt Ihre Zustimmung aus.<br/><br/>Frais d'envoi en supplément pour toute commande d'un montant inférieur à 150.00 € hors TVA.<br/>Extra vrachtkosten voor een bestelling onder aankoopbedrag van 150.00 € excl. BTW."))

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals.update({
            'header_text': self.header_text,
            'footer_text': self.footer_text,
        })
        
        return invoice_vals