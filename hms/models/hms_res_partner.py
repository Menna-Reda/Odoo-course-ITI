from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient', string='Related Patient')

    _sql_constraints = [
        ('related_patient_id_unique', 'UNIQUE(related_patient_id)', 'Each customer can have only one related patient!'),
   ]
   
    @api.constrains('vat')
    def check_customer_vat_mandatory(self):
        for rec in self:
            if not rec.vat:
                raise ValidationError('Tax ID is mandatory!')
    
    def unlink(self):
        for rec in self:
            if rec.related_patient_id:
                raise ValidationError("Cannot delete a customer linked to a patient!")
        return super().unlink()
