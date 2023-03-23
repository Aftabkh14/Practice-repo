from odoo import api, fields, models, _


class BeautyWizard(models.TransientModel):
    _name = "beauty.wizard"
    _description = "Create beauty Wizard"

    product_stts = fields.Selection(
        [('available', 'Available'), ('not available','Not available')],string='Product')
    product_id = fields.Many2one('beauty.shop', string="Product", required=True)
    delievery_date = fields.Datetime('Delievery Date')

    def update_fun(self):
        pass
