from odoo import fields, models, api


class ShkollaNxenes(models.Model):
    _name = 'shkolla.nxenes'
    _description = 'Description'

    name = fields.Char(string="Emri", required=True)
    mbiemer = fields.Char(string="Mbiemer", required=True)
    ditelindje = fields.Date(string='Ditelindje', required=True)
    nr_amez = fields.Integer(string="Nr. Amez", required=True)
    notat = fields.One2many(comodel_name='shkolla.notat', inverse_name='nxenes_id', string='Notat')
    nota_mesatare = fields.Float(compute='_compute_nota_mesatare', string='Nota Mesatare')

    @api.depends('notat')
    def _compute_nota_mesatare(self):
        for record in self:
            notat = record.notat.mapped('nota')
            s = 0
            for nota in notat:
                s += int(nota)
            record.nota_mesatare = s / len(notat)

    def bej_ekselent(self):
        for nota in self.notat:
            nota.nota = '10'


class ShkollaNotat(models.Model):
    _name = 'shkolla.notat'
    _description = 'ShkollaNotat'

    lenda = fields.Many2one(comodel_name='shkolla.lenda', string="Lenda", required=True)
    nxenes_id = fields.Many2one(comodel_name='shkolla.nxenes', string='Nxenes', required=True)
    nota = fields.Selection(string="Notat", required=True,
                            selection=[('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
                                       ('10', '10')])
