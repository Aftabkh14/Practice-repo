# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KfcClass(models.Model):
    _name = 'kfc.tbl'

    food_name = fields.Char('Fast Foods')
    weight = fields.Char('Food in wieght')
    packs = fields.Char('Food in Packs')
    price = fields.Char('Food Price')
