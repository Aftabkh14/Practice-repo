# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AppleIphoneClass(models.Model):
    _name = 'apple.iphone.company'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'This tbl is for Appple iphone company '

    c_name = fields.Char('Customer Name', tracking=1)
    c_cnic = fields.Char('Customer CNIC', tracking=1)
    c_address = fields.Char('Customer Address', tracking=1)
    c_phone = fields.Char('Customer Phone', tracking=1)
    c_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', default="male", tracking=1)

    status = fields.Selection([
        ('order', 'Order'),
        ('add to cart', 'Add To Cart'),
        ('cancel', 'Cancel'),
    ])

    mac_id = fields.Many2one('mac.tbl', string="Mac ID", tracking=1)
    ipad_id = fields.Many2one('ipad.tbl', string="iPad ID", tracking=1)
    iphone_id = fields.Many2one('iphone.tbl', string="iPhone ID", tracking=1)
    watch_id = fields.Many2one('watch.tbl', string="Watch ID", tracking=1)
    airpod_id = fields.Many2one('airpod.tbl', string="AirPod ID", tracking=1)

    price = fields.Float(string='Price')
    discount = fields.Float(string='Discount')
    total_price = fields.Float(compute="total_price_fun" ,string='Total Price')
    note = fields.Text('Description')





    def statusbar_order_func(self):
           self.status = 'order'

    def statusbar_add_to_cart_func(self):
        self.status = 'add to cart'

    def statusbar_cancel_func(self):
        self.status = 'cancel'

    # def mark_as_done(self):
    #     self.status = 'mark as done'

    @api.depends('price', 'discount')
    def total_price_fun(self):
        for rec in self:
            total = 0
            if rec.price:
                total = total + rec.price

            if rec.discount:
                total = total - rec.discount

            rec.total_price = total




class MacClass(models.Model):
    _name = "mac.tbl"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "This table is for Apple laptops"


    name = fields.Char('Name')

    models = fields.Selection([
        ('macbookair', 'MacBook Air'),
        ('macbook pro', 'MacBook Pro'),
        ('imac24', 'iMac 24'),
        ('mac mini', 'Mac Mini'),
        ('mac studio', 'Mac Studio'),
        ('mac pro', 'Mac Pro')
    ], string="Mac Models", tracking=1)

    displays = fields.Selection([
        ('studio display', 'Studio Display'),
        ('pro display xdr', 'Pro Display XDR'),
    ], string="Display", tracking=1)

    accessories = fields.Selection([
        ('magic trackpad', 'Magic Trackpad'),
        ('magic mouse', 'Magic Mouse'),
        ('mac showcase', 'Mac ShowCase'),
    ], string="Accessories", tracking=1)

    prices = fields.Float('Price', tracking=1)



class IpadClass(models.Model):
    _name = "ipad.tbl"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "This table is for Ipad models"
    _rec_name = "ipad_models"


    ipad_models = fields.Selection([
        ('ipad pro', 'iPad Pro'),
        ('ipad', 'iPad'),
        ('ipad mini', 'iPad Mini'),
        ('apple pencil', 'Apple Pencil'),
        ('ipad keyboards', 'iPad Keyboards')
    ], string="iPad Models", tracking=1)

    accessories = fields.Selection([
        ('smart keyboard', 'Smart Keyboard'),
        ('apple pencil', 'Apple pencil'),
        ('smart folio', 'Smart Folio'),
    ], string="Accessories", tracking=1)

    prices = fields.Float('Price')




class IphoneClass(models.Model):
    _name = 'iphone.tbl'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "This table is for iphone models"


    name = fields.Char('Name')
    iphone_models = fields.Selection([
        ('iphone14 pro', 'iPhone 14 Pro'),
        ('iphone 14', 'iPhone 14'),
        ('iphone 13 pro', 'iPhone 13 Pro'),
        ('iphone 13', 'iPhone 13'),
        ('iphone se', 'iPhone SE'),
        ('iphone 12 pro', 'iPhone 12 Pro'),
        ('iphone 12', 'iPhone 12'),
    ], string="iPhone Models", tracking=1)

    accessories = fields.Selection([
        ('iphone leather case', 'iPhone Leather case'),
        ('iphone clear case', 'iPhone Clear case'),
        ('iphone wallet', 'iPhone wallet'),
        ('iphone selicon case', 'iPhone Selicon Case'),
        ('iphone magesafe charger', 'iPhone Magesafe Charger')

    ], string="Accessories", tracking=1)

    prices = fields.Float('Price', tracking=1)


class WacthClass(models.Model):
    _name = "watch.tbl"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "wacth_models"
    _description = "This table is for wacth models"

    wacth_models = fields.Selection([
        ('apple wacth ultra', 'Apple Wacth Ultra'),
        ('apple wacth series 8', 'Apple Wacth Series 8'),
        ('apple wacth se', 'Apple Wacth SE'),
        ('apple wacth nike', 'Apple Wacth NIKE'),
        ('apple wacth hermes', 'Apple Wacth Hermes'),
        ('apple wacth studio', 'Apple Wacth Studio'),
    ], string="Wacth Models", tracking=1)

    wacth_bands = fields.Selection([
        ('black sport loop', 'Black Sport Loop'),
        ('black sport unity', 'Black Sport Unity Band'),
        ('orange alpine loop', 'Orange Alpine Loop'),
        ('gray trail loop', 'Gray Trail Loop'),
        ('yellow trail loop', 'Yellow Trail Loop'),
        ('midnight ocean band', 'Midnight Ocean Band'),
        ('white ocean band', 'White Ocean Band')
    ], string="Wacth Bands", tracking=1)

    wacth_accessories = fields.Selection([
        ('leather link', 'leather link'),
        ('sport band', 'Sport Band'),
        ('trail band', 'Trail Band'),
        ('ocean band', 'Ocean Band'),
        ('41mm black band', '41mm Black Uity Band'),

    ], string="Accessories", tracking=1)


    prices = fields.Float('Price')


class AirPodsClass(models.Model):
    _name = "airpod.tbl"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "airpods_models"
    _description = "Tis table is for Appple AirPods Models"

    airpods_models = fields.Selection([
        ('airpods 2nd generation', 'AirPods 2nd Generation'),
        ('airpods 3nd generation', 'AirPods 3nd Generation'),
        ('airpods pro 2nd generation', 'AirPods Pro 2nd Generation'),
        ('airpods max', 'AirPods Max')
    ], string="AirPods Models", tracking=1)

    prices = fields.Float('Price', tracking=1)






