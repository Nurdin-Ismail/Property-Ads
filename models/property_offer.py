from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError



class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    
    @api.depends('property_id', 'partner_id')
    def _compute_name(self):
        for rec in self:
            if rec.property_id and rec.partner_id:
                rec.name = f"{rec.property_id.name} - {rec.partner_id.name}"
            else:
                rec.name = False


    name= fields.Char(string="Name", compute = '_compute_name')
    price = fields.Float(string="Price")
    status = fields.Selection([('accepted', 'Accepted'), ('declined', 'Declined')], string="Status")
    partner_id = fields.Many2one('res.partner', string="Customers")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string="Validity")
    deadline = fields.Date(string="Deadline", compute='_compute_deadline', inverse='_inverse_deadline')
    
    @api.model
    def _set_create_date(self):
        return fields.Date.today()

    creation_date = fields.Date(string="Create Date", default=_set_create_date)

    @api.depends('validity', 'creation_date')
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    def _inverse_deadline(self):
        for rec in self:
            if rec.deadline and rec.creation_date:
                rec.validity = (rec.deadline - rec.creation_date).days
            else:
                rec.validity = 0


    def action_accept_offer(self):
        self._validate_accepted_offer()
        if self.property_id:
            self.property_id.selling_price = self.price
            self.property_id.state = 'accepted'
        self.status = 'accepted'



    def action_reject_offer(self):
        self.status = 'declined'
        all_declined = all(status != 'accepted' for status in self.property_id.offer_ids.mapped('status'))

        if all_declined:
            self.property_id.write({
            'selling_price': 0,
            
        })
            self.property_id.state = 'received'
        


    def _validate_accepted_offer(self):
        offer_ids = self.env['estate.property.offer'].search([
            ('property_id', '=', self.property_id.id),
            ('status', '=', 'accepted')
        ])
        
        if offer_ids:
            raise ValidationError("You have accepted an offer already")