from odoo import api, fields, models


class KursiPengantin(models.Model):
    _name = 'buku.bukukomik'
    _description = 'Daftar Buku Komik'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi buku Komik')
    stok = fields.Integer(string='Stok Buku Komik')
    harga = fields.Integer(string='Harga Buku')
