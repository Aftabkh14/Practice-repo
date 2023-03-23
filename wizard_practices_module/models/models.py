# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WizardPracticesClass(models.Model):
    _name = 'eurocup.franchises.home.tbl'
    _description = 'This table is for franchises home'
    _rec_name = "game_number"

    game_number = fields.Integer('Game')
    game_date = fields.Datetime('Date')
    Vanue = fields.Selection([
        ('itliano', 'Itliano'),
        ('paris di gurund', 'Paris Di Gurund'),
        ('rooma itliano', 'Rooma Itliano'),
    ], string="Game Vanue")
    refrees = fields.Selection([
        ('antony cin', 'Antony Cin'),
        ('myberg febian', 'Myberg Febian'),
        ('decosta parker', 'Decosta Parker'),
        ('liam tylor', 'Liam Tylor'),
    ], string="Game Refree")
    franchise_id = fields.Many2one("manchester.united.tbl", string="Franchise ID")
    broadcaster_id = fields.Many2one("broadcasters.tbl", string="BroadCaster ID")









class ManchesterUnitedClass(models.Model):
    _name = "manchester.united.tbl"
    _rec_name = "club_name"
    _description = "this table is for Manchester United Football Club"

    club_name = fields.Char('Club Name')
    total_players = fields.Char('Total Players')
    coach = fields.Char('Coach')
    own = fields.Char('Own')
    ceo = fields.Char('CEO')
    short_color = fields.Selection([
        ('red', 'Red'),
        ('red-white', 'Red-White'),
        ('red-black', 'Red-Black'),
    ], string="Shirt Color")


class BroadCastersClass(models.Model):
    _name = "broadcasters.tbl"
    _rec_name = "broadcaster_name"
    _description = "this table is for broadcasters of Euro cup"

    broadcaster_name = fields.Char('Broadcaster Name')
    own = fields.Char('Own')
    ceo = fields.Char('CEO')
    links = fields.Integer('Links')
