from odoo import api, fields, models


class Penerimaan(models.Model):
    _name = 'buku.penerimaan'
    _description = 'Paket yang telah diterima'

    name = fields.Char(compute='_compute_nama_pembeli', string='nama_pembeli')
    order_id = fields.Many2one('buku.order', string='No. Order')
    
    @api.depends('order_id')
    def _compute_nama_pembeli(self):
        for record in self:
            record.name = self.env['buku.order'].search([('id', '=', record.order_id.id)]).mapped('pemesan').name
    
    tgl_penerimaan = fields.Date(string='', default=fields.Date.today())
    
    tagihan = fields.Integer(compute='_compute_tagihan', string='tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total            
        
    @api.model
    def create(self,vals):
        record = super(Penerimaan, self).create(vals) 
        if record.tgl_penerimaan:
            self.env['buku.order'].search([('id','=',record.order_id.id)]).write({'barang_diterima':True}) 
            self.env['buku.akunting'].create({'kredit' : record.tagihan, 'name':record.name})          
            return record

    def unlink(self):
        for arif in self:
            self.env['buku.order'].search([('id','=',arif.order_id.id)]).write({'barang_diterima':False})
        record = super(Penerimaan, self).unlink()
   
        
            