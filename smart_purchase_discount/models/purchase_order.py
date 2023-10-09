from odoo import api, fields, models, _
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_discount = fields.Boolean(config_parameter='smart_purchase_discount.activate_discount')

    


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    discount = fields.Float("Discount")