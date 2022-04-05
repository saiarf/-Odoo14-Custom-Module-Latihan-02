from odoo import api, fields, models


class Buku(models.Model):
    _name = 'buku.daftarbuku'
    _description = 'New Description'

    name = fields.Char(string='Nama Paket Buku', required=True)
    bukukomik_id = fields.Many2one(comodel_name='buku.bukukomik', 
                                string='Tipe Buku Komik')   
    bukunovel_id = fields.Many2one(comodel_name='buku.bukunovel', 
                                        string='Tipe Buku Novel')

    harga = fields.Integer(compute='_compute_harga', string='Harga')
    
    @api.depends('bukukomik_id','bukunovel_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.bukukomik_id.harga + record.bukunovel_id.harga
    
    stok = fields.Integer(string='Stok Buku')
    
    des_bukukomik = fields.Char(compute='_compute_des_bukukomik', string='Deskripsi Buku Komik')
    
    @api.depends('bukukomik_id')
    def _compute_des_bukukomik(self):
        for record in self:
            record.des_bukukomik = record.bukukomik_id.deskripsi
    
    des_bukunovel = fields.Char(compute='_compute_des_bukunovel', string='Deskripsi Buku Novel')
    
    @api.depends('bukunovel_id')
    def _compute_des_bukunovel(self):
        for record in self:
            record.des_bukunovel = record.bukunovel_id.deskripsi
    
