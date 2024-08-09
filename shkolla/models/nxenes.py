from odoo import fields, models, api


class ShkollaNxenes(models.Model):
    _name = 'shkolla.nxenes'
    _description = 'Description'

    name = fields.Char(string="Emri", required=True)
    mbiemer = fields.Char(string="Mbiemer", required=True)
    ditelindje = fields.Date(string='Ditelindje', required=True)
    nr_amez = fields.Integer(string="Nr. Amez", required=True)
    notat = fields.One2many(comodel_name='shkolla.notat', inverse_name='nxenes_id', string='Notat')


class ShkollaNotat(models.Model):
    _name = 'shkolla.notat'
    _description = 'ShkollaNotat'

    lenda = fields.Char(string="Lenda", required=True)
    nxenes_id = fields.Many2one(comodel_name='shkolla.nxenes', string='Nxenes', required=True)
    nota = fields.Integer(string="Notat", required=True)

