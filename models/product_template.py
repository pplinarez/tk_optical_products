
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

"""
    def product_attributes(self, is_optical):
        attributes = ["Brand", "Rim", "Type of glasses", "style", "Gender"]
        product_attribute_lines =[]
        existing_attributes = []
        product_attribute_values=[]
        if is_optical == True:
            if self.attribute_lines_ids:
                pass
            else:  
                for line in self.attribute_lines_ids:
                    product_attribute_lines.append(line.display_name)
                    product_attribute_values.append(line.value_ids.name)

                    for attrs in product_attribute_lines:
                        if attrs not in attributes:
                            
                            existing_attributes.append(attrs)
                    
                    


      """"""          
        #product_attribute_lines = self.env["product.template.attribute_line_ids"].search()
        
        if self.attribute_line_ids: 
            pass
        else: 
            for attribute in attributes:
                values = {}
                values["active"]= True
                values["attribute_id"] = search
                create({"name": name })
"""
