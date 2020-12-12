# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ahmarcos_module(models.Model):
#     _name = 'ahmarcos_module.ahmarcos_module'
#     _description = 'ahmarcos_module.ahmarcos_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
