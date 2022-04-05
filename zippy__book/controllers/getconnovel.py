from odoo import http, fields, models
from odoo.http import request
import json


class BukuNovelCon(http.Controller):
    @http.route(['/bukunovel','/bukunovel/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getBukuNovel(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            kursi = request.env['buku.bukunovel'].search([])            
            for k in kursi:
                value.append({"id": k.id,
                            "namanovel" : k.name,
                            "stok_tersedia" : k.stok,
                            "harga_buku" : k.harga})
            return json.dumps(value)
        else:
            kursiid = request.env['buku.bukunovel'].search([('id','=',idnya)])
            for k in kursiid:
                value.append({"id": k.id,
                            "namakursi" : k.name,
                            "stok_tersedia" : k.stok,
                            "harga_buku" : k.harga})
            return json.dumps(value)
    
    @http.route('/createnovel',auth='user', type='json', methods=['POST'])
    def createNovel(self, **kw):    
        if request.jsonrequest:    
            if kw['name']:
                vals={
                    'name': kw['name'],
                    'stok' : kw['stok'],
                    'harga' : kw['harga'],
                }
                novelbaru = request.env['buku.bukunovel'].create(vals)
                args = {'success': True, 'ID':novelbaru.id}
                return args