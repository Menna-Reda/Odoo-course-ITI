from odoo import models, fields

class HMSDepartments(models.Model):
    _name = "hms.department"

    name = fields.Char(string="Name",required=True)
    capacity = fields.Integer(string="Capacity")
    is_opened = fields.Boolean(string="Is opened")
    patient_ids = fields.One2many(comodel_name = "hms.patient",inverse_name = "deparment_id" )





