from odoo import api, fields, models
from odoo.exceptions import ValidationError

#Order General
class Order(models.Model):
    _name = 'buku.order'
    _description = 'New Description'

    orderbuku_ids = fields.One2many('buku.orderbukudetail', inverse_name='order_id', string='Order Buku')
    ordernovel_ids = fields.One2many('buku.ordernoveldetail', inverse_name='orderk_id', string='Order Novel')

    name = fields.Char(string='Kode Pemesanan', required=True)
    tanggal_pemesanan = fields.Datetime('Tanggal Pemesanan',default=fields.Datetime.now())
    tanggal_pengiriman = fields.Date(string='Tanggal Pengiriman', default=fields.Date.today())
    pemesan = fields.Many2one('res.partner',  string='Pemesan', domain=[('is_customernya','=', True)],store=True)

    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    
    @api.depends('orderbuku_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['buku.orderbukudetail'].search([('order_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['buku.ordernoveldetail'].search([('orderk_id', '=', record.id)]).mapped('harga'))
            record.total = a + b
    
    barang_diterima = fields.Boolean(string='Barang Sudah Diterima', default=False)
    

#Oder Buku Detail
class OrderBukuDetail(models.Model):
    _name = 'buku.orderbukudetail'
    _description = 'New Description'

    order_id = fields.Many2one('buku.order', string='Order')
    buku_id = fields.Many2one('buku.daftarbuku', string='Paket Buku')   
    
    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='harga')
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('buku_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.buku_id.harga

    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self,vals):
        record = super(OrderBukuDetail, self).create(vals) 
        if record.qty:
            self.env['buku.daftarbuku'].search([('id','=',record.buku_id.id)]).write({'stok':record.buku_id.stok-record.qty})
            return record
            
#Order Novel Detail
class OrderNovelDetail(models.Model):
    _name = 'buku.ordernoveldetail'
    _description = 'New Description'
    
    orderk_id = fields.Many2one('buku.order', string='Order Novel')
    novel_id = fields.Many2one('buku.bukunovel', string='Buku Novel', domain=[('stok','>','5')])

    name = fields.Char(string='Name')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')

    @api.depends('novel_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.novel_id.harga
    
    qty = fields.Integer(string='Quantity')

    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            bahan = self.env['buku.bukunovel'].search([('stok', '<',record.qty),('id', '=',record.id)])
            if bahan:
                raise ValidationError("Stok Buku Novel yang dipilih tidak cukup")
    
    harga = fields.Integer(compute='_compute_harga', string='harga')

    @api.depends('harga_satuan','qty')
    def _compute_harga(self):
        for record in self:
               record.harga = record.harga_satuan * record.qty

    @api.model
    def create(self,vals):
        record = super(OrderNovelDetail, self).create(vals) 
        if record.qty:
            self.env['buku.bukunovel'].search([('id','=',record.novel_id.id)]).write({'stok':record.novel_id.stok-record.qty})
            return record
    
