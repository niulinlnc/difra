# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from odoo.addons import decimal_precision as dp
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


class MrpRepair(models.Model):
    _inherit = 'mrp.repair'

    # Set required=False
    product_id = fields.Many2one(
        'product.product', string='Product to Repair',
        readonly=True, required=False, states={'draft': [('readonly', False)]})
    product_qty = fields.Float(
        'Product Quantity',
        default=1.0, digits=dp.get_precision('Product Unit of Measure'),
        readonly=True, required=False, states={'draft': [('readonly', False)]})
    product_uom = fields.Many2one(
        'product.uom', 'Product Unit of Measure',
        readonly=True, required=False, states={'draft': [('readonly', False)]})

    repair_type = fields.Selection([('repair', 'Repair'), ('template', 'Template')], default='repair',
                                   string="Repair Type")
    template_id = fields.Many2one('mrp.repair', string="Template")
    claim_id = fields.Many2one('claim')
    case = fields.Selection(related="claim_id.case", readonly=True, default="company")
    delivery_address = fields.Many2one('res.partner', string="Delivery Address")
    description = fields.Text(related="claim_id.description")
    assigned_to = fields.Many2many('res.users', string="Assigned To")
    start_repair_date = fields.Date("Start Repair Date", readonly=True)
    start_repair_user_id = fields.Many2one('res.users', "Start Repair User", readonly=True)
    end_repair_date = fields.Date("End Repair Date", readonly=True)
    end_repair_user_id = fields.Many2one('res.users', "End Repair User", readonly=True)
    validation_date = fields.Date("Validation Repair Date", readonly=True)
    validation_user_id = fields.Many2one('res.users', "Validation Repair User", readonly=True)
    send_article = fields.Boolean("Product must be send ?")
    send_article_date = fields.Date("Date to send product")
    test_ids = fields.One2many('mrp_repair.test', 'repair_id', string="Tests",
                               default=lambda self: self._compute_default_tests())
    is_shipped = fields.Boolean(compute="_compute_is_shipped")
    is_delivered = fields.Boolean(compute="_compute_is_delivered")
    state = fields.Selection(selection_add=[('validated', 'Validated')])
    picking_ids = fields.Many2many('stock.picking', string="Receptions", compute='_compute_picking')
    picking_count = fields.Integer("Receptions", compute='_compute_len_picking')
    appointment_ids = fields.One2many('calendar.event', 'claim_id', string="Appointment",
                                      related="claim_id.appointment_ids")
    len_appointment_ids = fields.Integer(compute='_compute_len_appointment_ids')
    customer_reference = fields.Char()
    picking_in_created = fields.Boolean(default=False)
    operations = fields.One2many('mrp.repair.line', 'repair_id', 'Parts', copy=True, readonly=False,
                                 states={'validated': [('readonly', True)]})

    header_text = fields.Text(string="Optional header text")
    footer_text = fields.Text(string="Optional footer text")
    text_pro_forma = fields.Text(string="Pro-Forma Informations", store=True, default="Payment with BELFIUS BANK WELKENRAEDT\nSwift: GKCCBEBB\nAccount no. : 776-5993591-58\nIBAN BE95 7765 9935 9158\nAll bank costs to your charge")

    # Compute Method
    @api.multi
    def _compute_picking(self):
        for repair in self:
            pickings = self.env['stock.picking']
            product_ids = repair.operations.mapped('product_id').ids
            domain = [
                ('picking_id.origin', '=', repair.name),
                '|',
                ('product_id', '=', repair.product_id.id),
                ('product_id', 'in', product_ids)
            ]
            moves = self.env['stock.move'].search(domain)
            repair.picking_ids = pickings | moves.mapped('picking_id')

    @api.multi
    def _compute_len_appointment_ids(self):
        for repair in self:
            repair.len_appointment_ids = len(repair.appointment_ids)

    @api.multi
    def _compute_len_picking(self):
        for repair in self:
            repair.picking_count = len(repair.picking_ids)

    @api.depends('picking_ids', 'picking_ids.state')
    def _compute_is_shipped(self):
        for repair in self:
            if all([x.state in ['done', 'cancel'] for x in repair.picking_ids.search(
                    [('picking_type_id', '=', self.env.ref('claim.stock_picking_type_repair_IN').id),
                     ('origin', '=', repair.name)])]):
                if repair.claim_id and repair.claim_id.state == "pending":
                    repair.claim_id.write({'state': 'ready'})
                repair.is_shipped = True

    @api.depends('picking_ids', 'picking_ids.state')
    def _compute_is_delivered(self):
        for repair in self:
            if all([x.state in ['done', 'cancel'] for x in repair.picking_ids.search(
                    [('picking_type_id', '=', self.env.ref('claim.stock_picking_type_repair_OUT').id),
                     ('origin', '=', repair.name)])]):
                repair.is_delivered = True

    def _compute_default_tests(self):
        repairTest = self.env['mrp_repair.test']
        if len(self.test_ids) == 0:
            names = self.env['mrp_repair.default_test'].search([]).mapped('name')
            for name in names:
                res = repairTest.create({'name': name, 'repair_id': self.id})
                repairTest |= res
            return repairTest
        else:
            return self.test_ids

    # Onchange methods
    @api.multi
    @api.onchange('template_id')
    def onchange_template_id(self):
        for repair in self:
            if repair.template_id:
                # replace the fields from template
                repair.product_id = repair.template_id.product_id if repair.template_id.product_id else False
                repair.product_qty = repair.template_id.product_qty if repair.template_id.product_qty else False
                repair.product_uom = repair.template_id.product_uom if repair.template_id.product_uom else False
                repair.pricelist_id = repair.template_id.pricelist_id
                repair.invoice_method = repair.template_id.invoice_method
                repair.update({
                    'operations': [(5, 0, 0)],
                    'fees_lines': [(5, 0, 0)],
                    'test_ids': [(5, 0, 0)],
                })
                operations = []
                for op in repair.template_id.operations:
                    operations.append((0, 0, {
                        'name': op.name,
                        'product_id': op.product_id,
                        'product_uom_qty': op.product_uom_qty,
                        'product_uom': op.product_uom,
                        'type': op.type,
                        'location_dest_id': op.location_dest_id,
                        'location_id': op.location_id,
                    }))
                # repair.fees_lines = [(0, 0, repair.template_id.fees_lines)]
                tests = []
                for test in repair.template_id.test_ids:
                    tests.append((0, 0, {
                        'name': test.name,
                        'state': test.state,
                    }))

                repair.update({
                    'operations': operations,
                    'test_ids': tests,
                })
                repair.header_text = repair.template_id.header_text
                repair.footer_text = repair.template_id.footer_text

    # Button action
    @api.multi
    def action_make_products_back(self):
        if self.create_picking(True, False):
            self.picking_in_created = True

    @api.multi
    def action_view_picking(self):
        action = self.env.ref('stock.action_picking_tree_all')
        result = action.read()[0]

        # override the context to get rid of the default filtering on operation type
        result['context'] = {}
        pick_ids = self.mapped('picking_ids')
        # choose the view_mode accordingly
        if not pick_ids or len(pick_ids) > 1:
            result['domain'] = "[('id','in',%s)]" % pick_ids.ids
        elif len(pick_ids) == 1:
            res = self.env.ref('stock.view_picking_form', False)
            result['views'] = [(res and res.id or False, 'form')]
            result['res_id'] = pick_ids.id
        return result

    def _prepare_stock_move_line(self, picking, move):
        result = {
            'picking_id': picking.id,
            'move_id': move.id,
            'product_id': self.product_id.id,
            'product_uom_id': self.product_uom.id,
            'product_uom_qty': 0,
            'ordered_qty': self.product_qty,
            'date': self.create_date,
            'owner_id': picking.partner_id.id,
            'location_id': move.location_id.id,
            'location_dest_id': move.location_dest_id.id,
        }
        if self.lot_id:
            result['lot_id'] = self.lot_id.id
            result['product_uom_qty'] = self.product_qty
        return result

    def _create_stock_move_line(self, picking, move):
        return self.env['stock.move.line'].create(self._prepare_stock_move_line(picking, move))

    def _prepare_stock_move(self, picking):
        if self.product_id.type not in ['product', 'consu']:
            return {}
        return {
            'name': self.product_id.name or '',
            'product_id': self.product_id.id,
            'product_uom': self.product_uom.id,
            'product_uom_qty': self.product_qty,
            'date': self.create_date,
            'date_expected': self.send_article_date or self.create_date,
            'location_id': picking.location_id.id,
            'location_dest_id': picking.location_dest_id.id,
            'picking_id': picking.id,
            'partner_id': picking.partner_id.id,
            'state': 'draft',
            'company_id': picking.company_id.id,
            'picking_type_id': picking.picking_type_id.id,
            'origin': self.name,
            'route_ids': picking.picking_type_id.warehouse_id and [
                (6, 0, [x.id for x in picking.picking_type_id.warehouse_id.route_ids])] or [],
            'warehouse_id': picking.picking_type_id.warehouse_id.id
        }

    @api.multi
    def _create_stock_move(self, picking):
        self.ensure_one()
        vals = self._prepare_stock_move(picking)
        return self.env['stock.move'].create(vals)

    def _prepare_stock_picking_in(self, isPieces):
        if isPieces:
            return {
                'picking_type_id': self.env.ref('claim.stock_picking_type_repair_IN').id,
                'partner_id': self.partner_id.id,
                'date': self.create_date,
                'origin': self.name,
                'location_dest_id': self.env.ref('stock.stock.stock_location_scrapped').id,
                'location_id': self.env.ref('claim.stock_picking_type_repair_IN').default_location_src_id.id,
                'company_id': self.company_id.id,
                'repair_id': self.id
            }
        else:
            return {
                'picking_type_id': self.env.ref('claim.stock_picking_type_repair_IN').id,
                'partner_id': self.partner_id.id,
                'date': self.create_date,
                'origin': self.name,
                'location_dest_id': self.env.ref('claim.stock_picking_type_repair_IN').default_location_dest_id.id,
                'location_id': self.env.ref('claim.stock_picking_type_repair_IN').default_location_src_id.id,
                'company_id': self.company_id.id,
                'repair_id': self.id
            }

    def _prepare_stock_picking_out(self, isPieces):
        if isPieces:
            return {
                'picking_type_id': self.env.ref('claim.stock_picking_type_repair_OUT').id,
                'partner_id': self.partner_id.id,
                'date': self.create_date,
                'origin': self.name,
                'location_dest_id': self.env.ref('claim.stock_picking_type_repair_OUT').default_location_dest_id.id,
                'location_id': self.env.ref('stock.stock_location_stock').id,
                'company_id': self.company_id.id,
                'repair_id': self.id
            }
        else:
            return {
                'picking_type_id': self.env.ref('claim.stock_picking_type_repair_OUT').id,
                'partner_id': self.partner_id.id,
                'date': self.create_date,
                'origin': self.name,
                'location_dest_id': self.env.ref('claim.stock_picking_type_repair_OUT').default_location_dest_id.id,
                'location_id': self.env.ref('claim.stock_picking_type_repair_OUT').default_location_src_id.id,
                'company_id': self.company_id.id,
                'repair_id': self.id
            }

    @api.multi
    def create_picking(self, isInMove, isPieces):
        self.ensure_one()
        if isPieces:
            if self.operations.filtered(lambda x: x.type == 'remove'):
                picking_in = self.env['stock.picking'].create(self._prepare_stock_picking_in(isPieces))
            if self.operations.filtered(lambda x: x.type == 'add'):
                picking_out = self.env['stock.picking'].create(self._prepare_stock_picking_out(isPieces))
            for mrp_repair_line_id in self.operations:
                if mrp_repair_line_id.product_id.type == 'product':
                    if mrp_repair_line_id.type == 'add':
                        self._compute_stock_picking(picking_out, mrp_repair_line_id)
                    else:
                        self._compute_stock_picking(picking_in, mrp_repair_line_id)
        else:
            if self.product_id.type == 'product':
                if isInMove:
                    picking = self.env['stock.picking'].create(self._prepare_stock_picking_in(False))
                else:
                    picking = self.env['stock.picking'].create(self._prepare_stock_picking_out(False))
                move = self._create_stock_move(picking)
                move = move.filtered(lambda x: x.state not in ['done', 'cancel'])._action_confirm()
                move._action_assign()
        return True

    def _compute_stock_picking(self, picking, mrp_repair_line_id):
        move = self._create_stock_move_pieces(picking, mrp_repair_line_id)
        move = move.filtered(lambda x: x.state not in ['done', 'cancel'])._action_confirm()
        move._action_assign()

    def _create_stock_move_pieces(self, picking, mrp_repair_line_id):
        self.ensure_one()
        if self.product_id.type not in ['product', 'consu']:
            return self.env['stock.move'].create({})
        vals = {
            'name': mrp_repair_line_id.product_id.name or '',
            'product_id': mrp_repair_line_id.product_id.id,
            'product_uom': mrp_repair_line_id.product_uom.id,
            'product_uom_qty': mrp_repair_line_id.product_uom_qty,
            'date': self.create_date,
            'date_expected': self.send_article_date or self.create_date,
            'location_id': picking.location_id.id,
            'location_dest_id': picking.location_dest_id.id,
            'picking_id': picking.id,
            'partner_id': picking.partner_id.id,
            'state': 'draft',
            'company_id': picking.company_id.id,
            'picking_type_id': picking.picking_type_id.id,
            'origin': self.name,
            'route_ids': picking.picking_type_id.warehouse_id and [
                (6, 0, [x.id for x in picking.picking_type_id.warehouse_id.route_ids])] or [],
            'warehouse_id': picking.picking_type_id.warehouse_id.id
        }
        return self.env['stock.move'].create(vals)

    def _create_stock_move_line_pieces(self, picking, move, mrp_repair_line_id):
        vals = {
            'picking_id': picking.id,
            'move_id': move.id,
            'product_id': mrp_repair_line_id.product_id.id,
            'product_uom_id': mrp_repair_line_id.product_uom.id,
            'product_uom_qty': 0,
            'ordered_qty': mrp_repair_line_id.product_uom_qty,
            'date': self.create_date,
            'owner_id': picking.partner_id.id,
            'location_id': move.location_id.id,
            'location_dest_id': move.location_dest_id.id,
        }
        if self.lot_id:
            vals['lot_id'] = self.lot_id.id
            vals['product_uom_qty'] = self.product_qty
        return self.env['stock.move.line'].create(vals)

    @api.one
    def action_validate(self):
        self.ensure_one()
        result = self.action_repair_confirm()
        if self.case == 'site':
            self.create_picking(False, True)

    @api.multi
    def action_repair_start(self):
        for repair in self:
            res = super(MrpRepair, self).action_repair_start()
            if res:
                repair.start_repair_date = datetime.today()
                repair.start_repair_user_id = repair.env.uid
                # send pieces if on site
            return res

    @api.multi
    def action_repair_end(self):
        if self.filtered(lambda x: x.state != 'under_repair'):
            raise exceptions.UserError(_("Repair must be under repair in order to end reparation."))
        for repair in self:
            repair.write({'repaired': True})
            vals = {
                'state': 'done',
                'end_repair_date': datetime.today(),
                'end_repair_user_id': repair.env.uid,
            }
            repair.write(vals)
        return True

    @api.multi
    def action_make_appointment(self):
        return {
            'name': "Rendez-vous",
            'type': 'ir.actions.act_window',
            'res_model': 'calendar.event',
            'view_type': 'form',
            'view_mode': 'calendar,tree,form',
            'context': {'default_repair_id': self.id, "default_claim_id": self.claim_id.id}
        }

    @api.multi
    def action_repair_validate(self):
        for repair in self:
            vals = {'state': "validated"}
            vals['validation_date'] = datetime.today()
            vals['validation_user_id'] = repair.env.uid
            if self.is_shipped and self.case == 'company' or self.picking_in_created:
                self._company_make_operations_move(repair)
                self.create_picking(False, False)
            if not repair.invoiced and repair.invoice_method == 'after_repair':
                vals['state'] = '2binvoiced'
            repair.write(vals)

    def _company_make_operations_move(self, repair):
        moves = self.env['stock.move']
        for operation in repair.operations:
            move = self.env['stock.move'].create({
                'name': repair.name,
                'product_id': operation.product_id.id,
                'product_uom_qty': operation.product_uom_qty,
                'product_uom': operation.product_uom.id,
                'partner_id': repair.address_id.id,
                'location_id': operation.location_id.id,
                'location_dest_id': operation.location_dest_id.id,
                'move_line_ids': [(0, 0, {'product_id': operation.product_id.id,
                                          'lot_id': operation.lot_id.id,
                                          'product_uom_qty': 0,  # bypass reservation here
                                          'product_uom_id': operation.product_uom.id,
                                          'qty_done': operation.product_uom_qty,
                                          'package_id': False,
                                          'result_package_id': False,
                                          'owner_id': repair.partner_id.id,
                                          'location_id': operation.location_id.id,  # TODO: owner stuff
                                          'location_dest_id': operation.location_dest_id.id, })],
                'repair_id': repair.id,
                'origin': repair.name,
            })
            moves |= move
            operation.write({'move_id': move.id, 'state': 'done'})
            consumed_lines = moves.mapped('move_line_ids')
            produced_lines = move.move_line_ids
            moves |= move
            moves._action_done()
            produced_lines.write({'consume_line_ids': [(6, 0, consumed_lines.ids)]})

    @api.multi
    def action_repair_invoice_create(self):
        for repair in self:
            res = super(MrpRepair, self).action_repair_invoice_create()
            if res:
                if repair.state == 'done':
                    repair.write({'state': 'validated'})
                repair.invoice_id.write({
                    'partner_shipping_id': repair.delivery_address.id,
                    'customer_order_reference': repair.customer_reference,
                    'description': repair.description,
                    'product_id': repair.product_id.id,
                    'repair_id': self.id
                })
            return res

    @api.multi
    def action_repair_cancel(self):
        for repair in self:
            super(MrpRepair, self).action_repair_cancel()
            for picking in repair.picking_ids:
                picking.action_cancel()

    @api.multi
    def action_repair_cancel_draft(self):
        for repair in self:
            if repair.claim_id.exists() and repair.claim_id.state != 'new':
                repair.claim_id.action_set_new()
            else:
                super(MrpRepair, self).action_repair_cancel_draft()

    @api.multi
    def action_send_mail(self):
        res = super(MrpRepair, self).action_send_mail()
        if self.env.context.get('proforma', False):
            template_id = self.env.ref('claim.mrp_repair_send_pro_forma_invoice').id
            ctx = {
                'default_model': 'mrp.repair',
                'default_res_id': self.id,
                'default_use_template': bool(template_id),
                'default_template_id': template_id,
                'default_composition_mode': 'comment'
            }
            res['context'] = ctx
            _logger.debug("\n\nres: %s" % res)
        return res
