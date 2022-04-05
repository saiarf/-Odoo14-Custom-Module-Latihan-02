from odoo import api, fields, models


class Accounting(models.Model):
    _name = 'buku.akunting'
    _description = 'New Description'
    _order = 'id asc'

    name = fields.Char(string='Nama')
    id_ak = fields.Char(string='Kode Akunting')
    date = fields.Datetime(string='Date', default=fields.Datetime.now())
    debit = fields.Integer(string='Debit')
    kredit = fields.Integer(string='Kredit')
    saldo = fields.Float(compute='_compute_saldo', string='Saldo')
    
    @api.depends('debit','kredit')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id','<',record.id)],limit=1,order='date desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.kredit - record.debit
    
    
    
