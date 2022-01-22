# -*- coding : utf-8 -*-

from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string = 'Name', required=True)
    description = fields.Text()
    postcode = fields.Char(string = 'Postcode')
    date_availability = fields.Datetime('Date availability',readonly=True)
    expected_price = fields.Float('Expceted Price', required=True)
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ]
    )
