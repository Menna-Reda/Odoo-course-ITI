from odoo import models, fields

class HMSDoctor(models.Model):
    _name = 'hms.doctor'
    _rec_name = "first_name"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    image = fields.Image(string="Image")
    deparment_id = fields.Many2one(comodel_name="hms.department")
    department_capacity = fields.Integer(related = 'deparment_id.capacity')

