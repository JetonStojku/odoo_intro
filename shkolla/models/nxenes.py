from odoo import fields, models, api


class ShkollaNxenes(models.Model):
    _name = 'shkolla.nxenes'
    _description = 'Description'

    name = fields.Char(string="Emri", required=True)
    mbiemer = fields.Char(string="Mbiemer", required=True)
    ditelindje = fields.Date(string='Ditelindje', required=True)
    nr_amez = fields.Integer(string="Nr. Amez", required=True)
