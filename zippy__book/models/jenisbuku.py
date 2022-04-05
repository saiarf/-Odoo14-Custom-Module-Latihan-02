from odoo import api, fields, models


class JenisBuku(models.Model):
    _name = 'buku.jenisbuku'
    _description = 'Data tentang Buku dan stoknya'

    name = fields.Char(string='Name')
    tipe = fields.Selection(string='Tipe Buku', 
                            selection=[('novel','Buku Novel'), ('komik','Buku Komik')])
    stok = fields.Integer(string='Stok Buku')
    
    
