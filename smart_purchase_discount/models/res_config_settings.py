# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    activate_discount = fields.Boolean("Activate Discount")
    discount_method = fields.Selection( [('fixed', 'Fiixed'), ('percentage', 'Percentage'),])
    fixed_discount_amount = fields.Float("Fixed Discount Amount")