from odoo import models, fields, api


import logging
_logger = logging.getLogger(__name__)

class StockSerialLotTraceWizard(models.TransientModel):

    _name = 'stock.serial.lot.trace.wizard'

    serial_lot = fields.Char('Serial/lot to trace', required=True)
    lot_id = fields.Many2one('stock.production.lot', string="Serial/Lot")
    message = fields.Char(string="Message")

    result_found = fields.Boolean(string="Found the results", default=False)

    move_ids = fields.Many2many('stock.move', string="Moves")
    partner_id = fields.Many2one('res.partner', string="Partner")
    product_id = fields.Many2one('product.product', string="Product")

    @api.multi
    def trace_serial_lot(self):
        lot_ids = self.env['stock.production.lot'].search([('name', '=', self.serial_lot)])
        message_text = ""

        if (len(lot_ids) == 0):
            message_text = "Serial not found"
        else:
            message_text = ""
            self.lot_id = lot_ids
            message_text = "Serial found"

            # check if contains quants
            if (len(self.lot_id.quant_ids) == 0):
                message_text += "\nNot quant on this serial/lot"
            else:
                for q in self.lot_id.quant_ids.sorted(key=lambda q: q.in_date):
                    if q.location_id.usage == 'customer':
                        self.product_id = q.product_id.id
                        self.move_ids = q.history_ids
                        for h in q.history_ids.sorted(key=lambda q: q.date):
                            self.partner_id = h.picking_partner_id
                            break
                    if self.partner_id:
                        self.result_found = True
                        break;

        self.message = message_text
        return {
            'context': self.env.context,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'stock.serial.lot.trace.wizard',
            'res_id': self.id,
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new',
            }