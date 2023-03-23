from odoo import api, fields, models

class WizardModel(models.TransientModel):
    _name = 'wizard.model'

    choose_one = fields.Boolean(string="Choose")
    mac_id = fields.Many2one("mac.tbl", 'Select Mac')
    iphone_id = fields.Many2one("iphone.tbl", 'Select Iphone')
    name = fields.Char('Name')
    age = fields.Char('Age')

    def update_mac(self):
        pass


        # if self.mac_id:
        #     self.mac_id.name = self.name
        #
        # if self.iphone_id:
        #     self.iphone_id.name = self.name


