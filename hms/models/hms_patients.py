from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
from datetime import date

class HMSPatientHistoryLog(models.Model):
    _name = 'hms.patient.history.log'

    description = fields.Text(string="History log description")
    patient_id = fields.Many2one(comodel_name='hms.patient')


class HMSPatient(models.Model):
    _name = 'hms.patient'
    _description = 'HMS Patient'
    _rec_name = "first_name"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    birth_date = fields.Date(string="Birth Date")
    history = fields.Html(string="History")
    cr_ratio = fields.Float(string="CR Ratio")
    blood_type = fields.Selection([
        ('a','A'), ('b','B'), ('ab','AB'), ('o','O')
    ], string="Blood Type")
    pcr =fields.Boolean(string="PCR")
    image = fields.Image(string="Image", attachment=True)
    address = fields.Text(string="Address")
    age = fields.Integer( compute = 'calculate_age' , store=True)
    deparment_id = fields.Many2one(comodel_name="hms.department")
    department_capacity = fields.Integer(related = 'deparment_id.capacity')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], string="Condition", default='undetermined')
    doctor_ids = fields.Many2many('hms.doctor',string="Doctors")
    is_history_visible = fields.Boolean(string="Is History Visible", default=True)
    email = fields.Char(string="Email")
    history_log = fields.One2many('hms.patient.history.log', 'patient_id', string="History Log")

    _sql_constraints = [
        ('iti_student_unique_email' , 'UNIQUE(email)' , 'Email must be unique')
    ]

    @api.constrains('pcr', 'cr_ratio')
    def _check_cr_ratio_required(self):
        for rec in self:
            if rec.pcr and not rec.cr_ratio:
                raise ValidationError("CR Ratio is required when PCR is checked.")
    @api.constrains('email')
    def check_valid_email(self):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        for rec in self:
            if rec.email and not re.match(email_regex, rec.email):
                raise ValidationError("Please enter a valid email address.")
    
    @api.onchange('age')
    def onchange_age(self):
        if self.age and self.age < 30:
            self.pcr = True
            self.is_history_visible = False
            return {
                'warning': {
                    'title': 'PCR Changed Warning',
                    'message': 'PCR checked successfully'
                }
            }
        elif self.age and self.age < 50:
            self.is_history_visible = False
        else:
            self.is_history_visible = True

    @api.depends('birth_date')
    def calculate_age(self):
         for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                        (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day))
            else:
                rec.age = 1

    @api.onchange('state')
    def onchange_state(self):
        for rec in self:
            if rec.state:
                vals = {
                    'description' : 'state has been changed to %s'%rec.state,
                    'patient_id' : rec.id
                }
                rec.env['hms.patient.history.log'].new(vals)

