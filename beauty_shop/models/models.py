# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BeautyShop(models.Model):
    _name = 'beauty.shop'

    name = fields.Char("Product Name")
    seriel = fields.Char("Product Seriel")
    code = fields.Char("Product Code")
    size = fields.Char("Product Size")
    price = fields.Char("Product Price")














