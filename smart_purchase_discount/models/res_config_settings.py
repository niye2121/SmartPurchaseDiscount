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

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update({
            'activate_discount': self.env['ir.config_parameter'].sudo().get_param('smart_purchase_discount.activate_discount'), 
            'discount_method': self.env['ir.config_parameter'].sudo().get_param('smart_purchase_discount.discount_method'), 
            'apply_on': self.env['ir.config_parameter'].sudo().get_param('smart_purchase_discount.apply_on'), 
            'calculate': self.env['ir.config_parameter'].sudo().get_param('smart_purchase_discount.calculate'), 
            'fixed_discount_amount': self.env['ir.config_parameter'].sudo().get_param('smart_purchase_discount.fixed_discount_amount'), 
            'discount_account': self.env['ir.config_parameter'].sudo().get_param('smart_purchase_discount.discount_account'), 
         
        })
        return res

    def set_values(self):
        super().set_values()

        param = self.env['ir.config_parameter'].sudo()

        activate_discount = self.activate_discount or False
        discount_method = self.discount_method or False
        apply_on = self.apply_on or False
        calculate = self.calculate or False
        fixed_discount_amount = self.fixed_discount_amount or False
        discount_account = self.discount_account and self.discount_account.id or False

        param.set_param('smart_purchase_discount.activate_discount', activate_discount)
        param.set_param('smart_purchase_discount.discount_method', discount_method)
        param.set_param('smart_purchase_discount.apply_on', apply_on)
        param.set_param('smart_purchase_discount.calculate', calculate)
        param.set_param('smart_purchase_discount.fixed_discount_amount', fixed_discount_amount)
        param.set_param('smart_purchase_discount.discount_account', discount_account)
