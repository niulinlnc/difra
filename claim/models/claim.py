# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _
from datetime import datetime

import logging
_logger = logging.getLogger(__name__)


class Claim(models.Model):
    _name = 'claim'
    _inherit = ['mail.thread']
    _description = 'Represent the model of a claim expressed by a customer'

    # atomic fields
    name = fields.Char("Claim Reference", default=lambda self: _('New'), required=True, readonly=True)
    state = fields.Selection([('new', "New"), ('ready', "Ready"), ('pending', "Pending"), ('done', "Done"), ('cancel', "Cancel")], default="new", required=True, track_visibility='onchange')
    case = fields.Selection([('company', 'Company'), ('site', 'Site'), ('phone', 'Phone')], default="company", required=True, groups="")
    customer_satisfaction = fields.Selection([('0', 'None'), ('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Normal'), ('4', 'Good'), ('5', 'Very Good')], "Customer Satisfaction", track_visibility='onchange')
    product_qty = fields.Float("Product Quantity", default="1.0")
    incident = fields.Boolean("Incident")
    incident_justification = fields.Text("Incident Justification")
    complaint = fields.Boolean("Complaint")
    complaint_justification = fields.Text("Complaint Justification")
    complaint_non_investigated_justification = fields.Text("Justification if Complaint is not investigated")
    breakdown = fields.Boolean("Breakdown")
    description = fields.Text("Description", track_visibility='onchange')
    end_date = fields.Date("End Date", readonly=True)
    authority_competent_reporting = fields.Boolean("Reporting")
    authority_competent_justification = fields.Text("Justification if no report")
    breakdown_description = fields.Text("Description")
    breakdown_last_maintenance = fields.Date("Last Maintenance Date")
    breakdown_commissioning_year = fields.Date("Commissioning Year")
    breakdown_fall = fields.Boolean("Fall")
    breakdown_wrong_usage = fields.Boolean("Wrong Usage")
    breakdown_overvoltage = fields.Boolean("Overvoltage")
    breakdown_miss_maintenance = fields.Boolean("Miss maintenance")
    breakdown_other = fields.Boolean("Other")
    breakdown_other_description = fields.Text("Other Description")
    breakdown_when = fields.Selection([('before', "Before Use"), ('during', "During Use"), ('after', "After Use")], default="during")
    note = fields.Text(string="Note")
    responsible_notified = fields.Boolean("Responsible Notified", default=False)
    incident_notified = fields.Boolean("Incident Notified", default=False)
    active = fields.Boolean("Active", default=True, track_visibility='onchange')
    realized_actions = fields.Text(string="Actions Realized")
    trauma = fields.Selection([('yes', 'Yes'), ('no', 'No')], required=True)
    trauma_explanation = fields.Text()
    appointment_ids = fields.One2many('calendar.event', 'claim_id', string="Appointment")
    len_appointment_ids = fields.Integer(compute='_compute_len_appointment_ids')

    # relationnal fields
    contact_id = fields.Many2one('res.partner', "Contact", required=True, track_visibility='onchange')
    site_address = fields.Many2one('res.partner', "Site Address", help="Address to go where repair is on site")
    team_id = fields.Many2one('claim.as_team', "AAS Team", default=lambda self: self.env['claim.as_team'].search([], limit=1))
    product_id = fields.Many2one('product.product', "Product", required=True, track_visibility='onchange')
    tag_ids = fields.Many2many('claim.tag', string="Claim Tags")
    repair_id = fields.Many2one('mrp.repair', "repair", readonly=True)

    # related fields
    as_responsible = fields.Many2one('res.users', "AS Responsible", related='team_id.as_responsible_id', readonly=True, default=lambda self: self.env['claim.as_team'].search([], limit=1).as_responsible_id.id)
    quality_responsible = fields.Many2one('res.users', "Quality Responsible", related='team_id.quality_responsible_id', readonly=True, default=lambda self: self.env['claim.as_team'].search([], limit=1).quality_responsible_id.id)
    email = fields.Char(track_visibility='onchange')
    phone = fields.Char(track_visibility='onchange')
    mobile = fields.Char(track_visibility='onchange')
    lot_id = fields.Many2one('stock.production.lot', domain="[('product_id', '=', product_id)]", track_visibility='onchange')
    display_breakdown = fields.Boolean("Breakdown", related='breakdown', readonly=True)
    display_incident = fields.Boolean("Incident", related='incident', readonly=True)
    display_complaint = fields.Boolean("Complaint", related='complaint', readonly=True)
    product_received = fields.Boolean("Product Received", related='repair_id.is_shipped', readonly=True)
    tracking = fields.Selection("Tracking", related='product_id.tracking', readonly=True)

    @api.multi
    def _compute_len_appointment_ids(self):
        for repair in self:
            repair.len_appointment_ids = len(repair.appointment_ids)

    @api.multi
    @api.onchange('contact_id')
    def change_contact_info(self):
        for claim in self:
            claim.email = claim.contact_id.email
            claim.phone = claim.contact_id.phone
            claim.mobile = claim.contact_id.mobile

    @api.multi
    def action_notify_responsible(self):
        for claim in self:
            if claim.as_responsible.email:
                template_id = self.env.ref('claim.notify_as_responsible_mail_template')
                if template_id:
                    template_id.sudo().send_mail(self.ids[0], force_send=True)
                self.responsible_notified = True
            else:
                raise exceptions.ValidationError(_("AS Responsible must have an email address!"))

    @api.multi
    def action_notify_incident(self):
        for claim in self:
            if claim.as_responsible.email and claim.quality_responsible.email:
                template_id = claim.env.ref('claim.notify_incident_mail_template')
                if template_id:
                    template_id.sudo().send_mail(claim.ids[0], force_send=True)
                    claim.incident_notified = True
            else:
                raise exceptions.ValidationError(_("AS Responsible and Quality Responsible must have an email address!"))

    @api.multi
    def action_print(self):
        self.ensure_one()
        return self.env.ref('claim.claim_pdf_report').report_action(self)

    @api.multi
    def action_cancel(self):
        for claim in self:
            claim.write({'state': 'cancel'})
            if len(claim.repair_id) > 0 and claim.repair_id.state != 'cancel':
                claim.repair_id.action_repair_cancel()

    @api.multi
    def action_set_new(self):
        for claim in self:
            claim.responsible_notified = False
            claim.state = "new"
            if claim.repair_id.exists() and claim.repair_id.state != 'draft':
                claim.repair_id.action_repair_cancel_draft()

    def _prepare_repair(self):
        article_send = False
        if self.case == 'company':
            article_send = True
        return {
            'product_id': self.product_id.id,
            'product_uom': self.product_id.uom_id.id,
            'product_qty': self.product_qty,
            'lot_id': self.lot_id.id,
            'partner_id': self.contact_id.id,
            'pricelist_id': self.contact_id.property_product_pricelist.id,
            'partner_invoice_id': self.contact_id.id,
            'delivery_address': self.contact_id.id,
            'invoice_address': self.contact_id.id,
            'case': self.case,
            'description': self.description,
            'claim_id': self.id,
            'send_article': article_send,
            'location_dest_id': self.env.ref('stock.stock_location_customers').id,
            'location_id': self.env.ref('claim.stock_location_repair').id,
            'invoice_method': "after_repair",
        }

    @api.multi
    def action_create_repair(self):
        self.ensure_one()
        if not self.repair_id.exists():
            mrp = self.env['mrp.repair'].create(self._prepare_repair())
            self.repair_id = mrp
            if mrp.case == "company":
                mrp.create_picking(True, False)


    @api.multi
    def action_validate_as(self):
        for claim in self:
            if claim.product_id.tracking in ['serial', 'lot'] and not claim.lot_id:
                raise exceptions.ValidationError(
                    _("The selected product is set to be tracked by lot/serial, you have to provide one to go further."))
            claim.state = "ready"
            if claim.quality_responsible.email:
                template_id = claim.env.ref('claim.notify_claim_ready')
                if template_id:
                    template_id.sudo().send_mail(claim.ids[0], force_send=True)
            else:
                raise exceptions.ValidationError(
                    _("AS Responsible must have an email address!"))

    @api.multi
    def action_validate_quality(self):
        for claim in self:
            claim.end_date = datetime.today()
            claim.state = "done"

    @api.multi
    def action_wait_product(self):
        for claim in self:
            #claim._create_picking()
            claim.state = "pending"

    @api.multi
    def action_view_repair(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'mrp.repair',
            'views': [[False, "form"]],
            'res_id': self.repair_id.id,
        }

    @api.multi
    @api.depends('repair_id.is_shipped')
    def _compute_state(self):
        _logger.debug("\n\nstate")
        for claim in self:
            if claim.state not in ["done", "cancel"] and claim.repair_id.exists() and claim.repair_id.is_shipped is True:
                claim.state = "ready"

    @api.model
    def _default_picking_type(self):
        type_obj = self.env['stock.picking.type']
        company_id = self.env.context.get('company_id') or self.env.user.company_id.id
        types = type_obj.search([('code', '=', 'incoming'), ('warehouse_id.company_id', '=', company_id)])
        if not types:
            types = type_obj.search([('code', '=', 'incoming'), ('warehouse_id', '=', False)])
        return types[:1]

    @api.one
    def generate_url(self):
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        if base_url and base_url[-1:] != '/':
            base_url += '/'
        return "{}web?#id={}&view_type=form&model={}".format(base_url, self.id, self._name)

    @api.model
    def create(self, vals):
        # Replace name "New" By good one with sequence number at creation
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('claim') or _('New')
        return super(Claim, self).create(vals)

    @api.multi
    def action_make_appointment(self):
        return {
            'type': 'ir.actions.act_window',
            'name':"Rendez-vous",
            'res_model': 'calendar.event',
            'view_type': 'form',
            'view_mode': 'calendar,tree,form',
            'context': {'default_claim_id': self.id, "default_repair_id": self.repair_id.id}
        }