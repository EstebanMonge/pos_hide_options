# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError





class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = ['product.template',]

    car_parts_characteristics = fields.Char()
    car_parts_compatibility = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
