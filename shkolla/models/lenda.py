from odoo import fields, models


class ShkollaLenda(models.Model):
    _name = 'shkolla.lenda'

    name = fields.Char(string='Lenda', required=True)
