from odoo import models,fields
from odoo import api, fields, models

class WizardModel(models.TransientModel):
    _name = 'apple.home.wizard'

    name = fields.Char('Name')
    mac_id = fields.Many2one("mac.tbl", 'Select Mac')
    iphone_id = fields.Many2one("iphone.tbl", 'Select Iphone')
    ipad_id = fields.Many2one("ipad.tbl", 'Select iPad')


    def update_mac(self):
        if self.mac_id:
            self.mac_id.name = self.name

        if self.iphone_id:
            self.iphone_id.name = self.name



