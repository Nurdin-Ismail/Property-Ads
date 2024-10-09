from odoo import fields, models, api

class Property(models.Model):
    _name = 'estate.property'

    name = fields.Char(string="Name")

    def action_accept(self):
        self.state = 'sold'

    def action_reject(self):
        self.state = 'rejected'

    state= fields.Selection([('new', 'New'),('received', 'Offer Recieved'),('accepted', 'Offer Accepted'),('sold', 'Sold'),('rejected', 'Rejected')], default='new', string="Status", group_expand="_expand_state")
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tag")
    type_id= fields.Many2one('estate.property.type', string="Property Type")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="postcode")
    date_availability = fields.Date(string="Available from")
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Best Offer", compute="compute_best_offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([('north', 'North'),('south', 'South'),('east', 'East'),('west', 'West'),],string="Garden Orientation", default="north")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer", domain=[('is_company', '=', 'True')])
    phone = fields.Char(string="Phone", related='buyer_id.phone')
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for rec in self:
            rec.total_area = rec.living_area + rec.garden_area

    total_area = fields.Integer(string="Total Area(sqm)", compute='_compute_total_area')

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)


    offer_count = fields.Integer(string="Offer Count", compute="_compute_offer_count")

    def _expand_state(self, states, domain, order):
        return [
            key for key, dummy in type(self).state.selection
        ]
    
    @api.depends('offer_ids')
    def compute_best_offer(self):
        for rec in self:
            if rec.offer_ids:
                rec.best_offer = max(rec.offer_ids.mapped('price'))
            else:
                rec.best_offer = 0


class PropertyType(models.Model):
    _name = 'estate.property.type'

    name = fields.Char(string="Name", required="True")


class PropertyTag(models.Model):
    _name = 'estate.property.tag'

    name = fields.Char(string="Name", required="True")
    color = fields.Integer(string="Color")