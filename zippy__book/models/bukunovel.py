from odoo import api, fields, models


class KursiPengantin(models.Model):
    _name = 'buku.bukunovel'
    _description = 'Daftar Buku Novel'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi Buku Novel')
    stok = fields.Integer(string='Stok Buku Novel')
    harga = fields.Integer(string='Harga Buku')