# -*- coding: utf-8 -*-

from odoo import models, fields
class zad_medical(models.Model):
    _name = 'zad_medical.zad_medical'
    _description = 'zad medical'

    name = fields.Char(string="Title" , required="true")
    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
