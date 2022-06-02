from odoo import models, fields, api, _
from types import SimpleNamespace
import logging

_logger = logging.getLogger(__name__)


class Member(models.Model):
    _name = 'agriculture.member'
    _inherit = 'mail.thread'
    _description = 'Member of agriculture app'
    _rec_name = 'SellerName'
    _order = "SellerName desc"

    SellerName = fields.Char(required=False)
    SellerId = fields.Char(string='SellerId', required=True,
                           readonly=True, default=lambda self: _(' '))
    FarmerType = fields.Selection(
        [('non_contract', '非契作農民'), ('contract', '契作農民')], string='FarmerType', default='non_contract', required=False)
    Region = fields.Char(required=False)
    AuxId = fields.Char(required=False)

    ContractArea = fields.Float(default=0.0, required=False)
    ChishangRArea = fields.Float(default=0.0, required=False)
    TGAPArea = fields.Float(default=0.0, required=False)

    OrganicVerifyDate = fields.Date(
        'OrganicVerifyDate', required=False)  # 有機認證日期

    OrganiCertifiedArea = fields.Float(default=0.0, required=False)
    NonLeasedArea = fields.Float(default=0.0, required=False)

    MaxPurchaseQTY = fields.Float(compute='_compute_QTY')

    @api.depends('ContractArea')
    def _compute_QTY(self):
        params = self.env['ir.config_parameter'].sudo()
        maxPurchaseQTYPerHectare = float(params.get_param(
            'agriculture.maxPurchaseQTYPerHectare'))
        for rec in self:
            rec.MaxPurchaseQTY = rec.ContractArea * maxPurchaseQTYPerHectare

    @api.model
    def create(self, fields):
        if fields.get('SellerId', _(' ')) == _(' '):
            fields['SellerId'] = self.env['ir.sequence'].next_by_code(
                'agriculture.member') or _(' ')
        res = super(Member, self).create(fields)
        return res

    def get_partner_attr(self, attr):
        for rec in self:
            _partner = self.env['res.partner']
            partnerData = _partner.search(
                [("SellerId", "=", rec.SellerId)], limit=1)
            if partnerData:
                if attr == 'address':
                    return "({zip}) {country}{city}{state}{street}{street2}".format(
                        zip=partnerData['zip'], country=partnerData['country_id'].name, city=partnerData['city'], state=partnerData['state_id'].name, street=partnerData['street'], street2=partnerData['street2'])
                else:
                    return partnerData[attr]

    def get_bank_info(self):
        empty = {}
        empty['acc_number'] = ""
        empty['bank_name'] = ""
        emptObj = SimpleNamespace(**empty)

        for rec in self:
            _partner = self.env['res.partner']
            partnerData = _partner.search(
                [("SellerId", "=", rec.SellerId)], limit=1)
            if not partnerData:
                return emptObj
            if not partnerData['bank_ids']:
                return emptObj
            if not partnerData['bank_ids'][0]:
                return emptObj
            return partnerData['bank_ids'][0]
        return emptObj
