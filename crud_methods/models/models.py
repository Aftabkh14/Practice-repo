# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SportsClasses(models.Model):
    _name = 'sports.tbl'
    _description = 'crud_methods'

    bat_name = fields.Char('Bat Name', required=1)
    bat_color = fields.Char('Bat Color')
    bat_price = fields.Float('Bat Price', required=1)
    bat_weight = fields.Char('Bat Weight')
    bat_number = fields.Char('Bat Contacts', copy=False)
    bat_lenght = fields.Char('Bat Lenght')
    bat_company = fields.Many2one('sports.company', string="Bat Company")


    # @api.onchange('bat_color')
    # def _onchange(self):
    #     self.bat_price = self.bat_color * 5


    # @api.model
    # def create(self, vals_list):
    #     if vals_list['bat_name'] == 'CA':
    #         raise ValidationError('Name is Already exist.')
    #     res = super().create(vals_list)
    #     return res
    #
    # def write(self, vals):
    #     if vals['bat_name'] == 'CA':
    #         raise ValidationError('Name is Already exist.')
    #     res = super().write(vals)
    #     return res
    #
    # def unlink(self):   #     delete method for record if you do not want to delete record restrict it with unlink method
    #     print('only testing the unlink mwthod that it is working or  not')
    #     if self.bat_name == 'khan':
    #         raise ValidationError('Cannot be deleted...')
    #
    #     return super(SportsClasses, self).unlink()


    # def unlink(self):
    #     for name in self:
    #         if name.bat_company:
    #             raise ValidationError('kkkkkkkk lol')
    #         return super(SportsClasses, self).unlink()





    # @api.model
    # def create(self, vals_list):
    #     if len(vals_list['bat_number']) == 11:        # this is used for to do not store invalid number from user
    #         if len(vals_list['bat_number']) > 11:  # this is used for to do not store invalid number from user
    #             vals_list['bat_number']
    #     else:
    #         raise ValidationError('Invalid phone number')  # error

    #     vals_list['bat_color'] = vals_list['bat_color'] + ' orignal'  # use for add original to color
    #     if vals_list['bat_name'] == 'CA':  # use for to do not store name that already exist in records
    #         raise ValidationError('This name already exist in record')

    #     res = super().create(vals_list)
    #     res.bat_price = res.bat_price + 1000
    #     return res


    # def write(self, vals):
    #     if vals['bat_name'] == 'CA':   # using write method here to still do not store the edited record
    #         raise ValidationError('This name already exist in record')  # error
    #     res = super().write(vals)
    #     return res


class CompanyClass(models.Model):
    _name = "sports.company"
    _description = "Sportss company"

    name = fields.Char('Company Name')
    name_no = fields.Char('Company Seriel')
