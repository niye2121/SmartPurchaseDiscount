# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    activate_discount = fields.Boolean("Activate Discount")
    discount_method = fields.Selection( [('fixed', 'Fixed'), ('percentage', 'Percentage'),], default='percentage')
    apply_on = fields.Selection( [('order_line', 'Order Line'), ('total', 'Total Value'),], default='order_line')
    calculate = fields.Selection( [('including_tax', 'Including Tax'), ('exclude_tax', 'Excluding tax'),], default='exclude_tax')
    fixed_discount_amount = fields.Float("Fixed Discount Amount")
    discount_account = fields.Many2one('account.account')