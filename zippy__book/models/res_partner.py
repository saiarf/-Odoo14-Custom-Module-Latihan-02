from odoo import api, fields, models


class ResPartner(models.AbstractModel):

    _inherit = 'res.partner'
    
    is_pegawainya = fields.Boolean(string='Pegawai', default=False)
    is_customernya = fields.Boolean(string='Pemesan', default=False)

