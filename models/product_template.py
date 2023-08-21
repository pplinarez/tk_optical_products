
from odoo import models, fields, api


class TKOpticalProduct(models.Model):
    _inherit = "product.template"

    is_optical = fields.Boolean(
        string = " Is a Optical product?"
    )  

    typeg = fields.Many2one("tk.type", 
        string = "Type of glasses")

    stylename = fields.Char(    
        string = "style")

    size = fields.Integer(
        string = "Size")

    material = fields.Many2one("tk.material",
        string = "Material")
        
    rim = fields.Many2one("tk.rim", 
        string = 'Rim') 

    color = fields.Char(
        string = "Color")

    country_id = fields.Many2one("res.country",
        string = "Country of Origin")

    gender= fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("unisex", "Unisex"),
        ("kids", "kids")],
        string = "Gender")

    product_brand_id = fields.Many2one(
        "product.brand", string="Brand")    