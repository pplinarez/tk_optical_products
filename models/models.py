# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TkMaterial(models.Model):
    _name = "tk.material"
    _description = "Material (Steel, wood, titanium, etc)"
    description = fields.Char()
    name = fields.Char(
        string = "Material")

class TkRim(models.Model):
    _name = "tk.rim"
    _description = "glasses rims (Full-rimmed, Rimless, Semi-rimless)"
    name = fields.Char(
        string = "Glasses Rim") 
    

class TkOpticalType(models.Model):
    _name = "tk.type"
    _description = "type of glasses (sunglasses, readdinglasses, etc)"
    description = fields.Char()
    name = fields.Char(
        string = "Type of glasses")