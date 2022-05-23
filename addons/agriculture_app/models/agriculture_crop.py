# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import api, fields, models
import logging
import requests

_logger = logging.getLogger(__name__)


class Crop(models.Model):
    _name = "agriculture.crop"
    _inherit = 'mail.thread'
    _rec_name = 'SeqNumber'
    _description = "Crop"
    _order = "EndTime desc"

    # ******主要使用資料******
    # ******流水號******
    SeqNumber = fields.Char(
        "SeqNumber",  required=False, readonly=True)
    # ******農夫的資訊從member中取得******
    SellerName = fields.Many2one(
        "agriculture.member", string="SellerName", required=False)
    SellerId = fields.Char(
        "SellerId", related="SellerName.SellerId", required=False)

    Region = fields.Char(
        "Region", related="SellerName.Region", required=False)
    AuxId = fields.Char("AuxId", related="SellerName.AuxId", required=False)
    FarmerType = fields.Selection(
        "FarmerType", related="SellerName.FarmerType", required=False)
    # *******************************************
    # ******農作物資料******
    FarmingMethod = fields.Selection([('conventional', '慣行農法'), (
        'organic', '有機耕作')], string='FarmingMethod', required=False)

    CropVariety = fields.Many2one(
        'agriculture.cropvariety', string='CropVariety', required=False)  # 品種 不同品種有不同的加成

    CropVariety_bonus = fields.Integer(
        'CropVariety_bonus', related="CropVariety.CropVariety_bonus", required=False)  # 品種加成bonus

    CropStatus = fields.Selection(
        [('dry', '乾穀'), ('humi', '濕穀')], 'CropStatus', required=False)  # 乾穀 濕穀

    CropType = fields.Selection([('a', '越光米'), (
        'b', '紅/黑糯米'), ('c', '糯米')], string='CropType', required=False)  # 特殊米種

    isTGAP = fields.Boolean(
        string="isTGAP", default=False)  # 是否TAGP yes = +100

    FarmingAdaption = fields.Selection(
        [('a', '有機轉型'), ('b', '隔離帶')], string='FarmingAdaption', required=False)  # 農業轉型

    BrownYield = fields.Float(
        'BrownYield', required=True, default=0.0)  # 糙米成品率

    HullYield = fields.Float('HullYield', required=True,
                             default=0.0)  # 粗糠成品率

    BranYield = fields.Float('BranYield', required=True,
                             default=0.0)  # 米糠成品率

    PrimeYield = fields.Float(
        'PrimeYield', required=True, default=0.0)  # 白米成品率

    BBRiceYield = fields.Float(
        'BBRiceYield', required=True, default=0.0)  # 大碎米成品率

    SBRiceYield = fields.Float(
        'SBRiceYield', required=True, default=0.0)  # 小碎米成品率

    RawHumidity = fields.Float(
        'RawHumidity', required=True, default=0.0)  # 稻穀濕度

    BrownHumidity = fields.Float(
        'BrownHumidity', required=True, default=0.0)  # 糙米濕度

    RiceHumidity = fields.Float(
        'RiceHumidity', required=True, default=0.0)  # 白米濕度

    BrownIntactRatio = fields.Float(
        'BrownIntactRatio', required=True, default=0.0)  # 糙米-完整粒

    BrownCrackedRatio = fields.Float(
        'BrownCrackedRatio', required=True, default=0.0)  # 糙米-胴裂粒

    BrownImmatureRatio = fields.Float(
        'BrownImmatureRatio', required=True, default=0.0)  # 糙米-未熟粒

    BrownPestsRatio = fields.Float(
        'BrownPestsRatio', required=True, default=0.0)  # 糙米-被害粒

    BrownColoredRatio = fields.Float(
        'BrownColoredRatio', required=True, default=0.0)  # 糙米-染色粒

    BrownDeadRatio = fields.Float(
        'BrownDeadRatio', required=True, default=0.0)  # 糙米-死米

    TasteRating = fields.Float(
        'TasteRating', required=True, default=0.0)  # 食味值

    Protein = fields.Float('Protein', required=True, default=0.0)  # 蛋白質含量

    BrownMoisture = fields.Float(
        'BrownMoisture', required=True, default=0.0)  # 遠紅外線-糙米濕度

    BrownAmylose = fields.Float(
        'BrownAmylose', required=True, default=0.0)  # 直鏈性澱粉含量

    VolumeWeight = fields.Float(
        'VolumeWeight', required=True, default=0.0)  # 容量重量

    CarCropWeight = fields.Float(
        'CarCropWeight', required=True, default=0.0)  # 重車重量

    CarWeight = fields.Float('CarWeight', required=True, default=0.0)  # 車重

    HarvestYear = fields.Integer(
        'HarvestYear', required=True, default=0)  # 收穫年份 民國年

    HarvestPeriod = fields.Integer(
        'HarvestPeriod', required=True, default=0)  # 期數

    LastCreationTime = fields.Datetime(
        'LastCreationTime', default=datetime.now())  # 收購時間

    CropWeight = fields.Float(
        'CropWeight', required=True, default=0.0)  # 稻穀總重量

    RawTotalWeight = fields.Float(
        'RawTotalWeight', required=True, default=0.0)

    BrownWeight = fields.Float(
        'BrownWeight', required=True, default=0.0)  # 糙米總重量

    HullWeight = fields.Float(
        'HullWeight', required=True, default=0.0)  # 粗糠總重量

    BranWeight = fields.Float(
        'BranWeight', required=True, default=0.0)  # 米糠總重量

    PrimeWeight = fields.Float(
        'PrimeWeight', required=True, default=0.0)  # 白米總重量

    BBRiceWeight = fields.Float(
        'BBRiceWeight', required=True, default=0.0)  # 大碎米總重量

    SBRiceWeight = fields.Float(
        'SBRiceWeight', required=True, default=0.0)  # 小碎米總重量

    WasteRatio = fields.Float('WasteRatio', required=True, default=0.0)

    BuyPrice = fields.Float('BuyPrice', required=True, default=0.0)

    MachineTime = fields.Integer('MachineTime', required=True, default=0)

    MachineUses = fields.Integer('MachineUses', required=True, default=0)

    MachineStatus = fields.Char('MachineStatus', required=True, default='')

    TotalLoadWeight = fields.Float(
        'TotalLoadWeight', required=True, default=0.0)

    LastEditTime = fields.Datetime('LastEditTime', default=datetime.now())

    WhiteAmylose = fields.Float('WhiteAmylose', required=True, default=0.0)

    WhiteProtein = fields.Float('WhiteProtein', required=True, default=0.0)

    WhiteQEV = fields.Float('WhiteQEV', required=True, default=0.0)

    WhiteMoisture = fields.Float('WhiteMoisture', required=True, default=0.0)

    WhiteIntactRatio = fields.Float(
        'WhiteIntactRatio', required=True, default=0.0)

    WhiteColoredRatio = fields.Float(
        'WhiteColoredRatio', required=True, default=0.0)

    WhiteCrackedRatio = fields.Float(
        'WhiteCrackedRatio', required=True, default=0.0)

    WhiteDeadRatio = fields.Float('WhiteDeadRatio', required=True, default=0.0)

    WhiteImmatureRatio = fields.Float(
        'WhiteImmatureRatio', required=True, default=0.0)

    WhitePestsRatio = fields.Float(
        'WhitePestsRatio', required=True, default=0.0)

    WetDryRatio = fields.Float('WetDryRatio', required=True, default=0.0)

    DryingFee = fields.Float('DryingFee', required=True, default=0.0)

    StorageId = fields.Char('StorageId', required=False)  # 存放的倉庫編號
    DryerId = fields.Char('DryerId', required=False)  # 洗米機編號

    # ******次要資料******

    StartTime = fields.Datetime('Start Time', required=False)
    StartTime_Date = fields.Char('Start Time Date', required=False)
    StartTime_Time = fields.Char('Start Time Time', required=False)

    EndTime = fields.Datetime('End Time', required=False)
    EndTime_Date = fields.Char('End Time Date', required=False)
    EndTime_Time = fields.Char('End Time Time', required=False)

    # active = fields.Boolean("Active?", default=True)
    archived_id = fields.Many2one("agriculture.archived")

    # new state

    @ api.model
    def _default_stage(self):
        Stage = self.env['crop.stage']
        return Stage.search([("state", "=", "draft")], limit=1)

    @ api.model
    def _done_stage(self):
        Stage = self.env['crop.stage']
        return Stage.search([("state", "=", "done")], limit=1)

    @ api.model
    def _archived_stage(self):
        Stage = self.env['crop.stage']
        return Stage.search([("state", "=", "archived")], limit=1)

    stage_id = fields.Many2one('crop.stage', default=_default_stage,
                               copy=False, group_expand="_group_expand_stage_id")
    state = fields.Selection(related="stage_id.state")

    def button_refresh(self):
        Stage = self.env['crop.stage']
        draft_stage = Stage.search([("state", "=", "draft")], limit=1)
        # for checkout in self:
        #     checkout.stage_id = done_stage
        return True

    # ******計價資料*****
    # 以計算完成定價
    PriceState = fields.Selection(
        [('draft', '草稿'), ('done', '計價完成'), ('archived', '完成出單')], string='PriceState', default='draft')
    # 底價判斷   底價 / 百台斤
    FinalPrice = fields.Float(
        "FinalPrice (/百台斤)", compute="_compute_final_price", store=True)

    # 總價加成
    TotalPrice = fields.Float(
        "TotalPrice (新台幣)", compute="_compute_total_price", store=True)

    @ api.depends('FarmerType',
                  'CropType',
                  'FarmingMethod',
                  'CropVariety_bonus',
                  'VolumeWeight',
                  'PrimeYield',
                  'TasteRating',
                  'BrownIntactRatio',
                  'FarmingAdaption',
                  'isTGAP')
    def _compute_final_price(self):
        for record in self:
            if self._check_nValue(record.VolumeWeight, record.PrimeYield, record.TasteRating, record.BrownIntactRatio):
                if record.FarmerType == 'contract':
                    # 契約農民
                    # 特殊米種
                    if record.CropType == 'a':
                        # 越光米
                        record.FinalPrice = 2600

                    elif record.CropType == 'b':
                        # 黑糯米或紅糯米
                        record.FinalPrice = 2400
                    elif record.CropType == 'c':
                        # 糯米
                        record.FinalPrice = 1700
                    else:
                        # 其他
                        # 有機米
                        if record.FarmingMethod == 'organic':
                            v = True if record.VolumeWeight >= 610 else False
                            v2 = True if record.VolumeWeight <= 610 and record.VolumeWeight > 560 else False
                            if v is False and v2 is True:
                                record.FinalPrice = 2400
                            elif v is True and record.PrimeYield > 70:
                                record.FinalPrice = 2600
                            elif v is True and record.PrimeYield < 70:
                                record.FinalPrice = 2400
                        else:
                            # 有機轉型或隔離帶
                            if record.FarmingAdaption == 'a' or record.FarmingAdaption == 'b':
                                record.FinalPrice = 2200
                            else:
                                # 慣行耕作
                                compare_list = [self._get_quality_level(record.TasteRating), self._get_quality_level(
                                    record.VolumeWeight), self._get_quality_level(record.BrownIntactRatio)]
                                min_value = min(compare_list)
                                bonus = self._get_compare_price(
                                    min_value, record.PrimeYield) + record.CropVariety_bonus
                                if record.isTGAP:
                                    record.FinalPrice = bonus + 100
                                else:
                                    record.FinalPrice = bonus

                else:
                    # 非契約農民
                    record.FinalPrice = 1400  # 增加 議價金額（正負）

                record.PriceState = 'done'
                self.stage_id = self._done_stage()
            else:
                record.FinalPrice = 0
                record.PriceState = 'draft'
                self.stage_id = self._default_stage()

    def _get_quality_level(self, expValue):
        p_list = [609.0, 590.0, 560.0, 540.0]
        x1 = expValue - p_list[3]
        x2 = expValue - p_list[0]
        x3 = expValue - p_list[1]
        x4 = expValue - p_list[2]

        lx1 = 1 if x1 >= 0 else -1
        lx2 = 1 if x2 > 0 else 0
        lx3 = 1 if x3 > 0 else 0
        lx4 = 1 if x4 > 0 else 0

        return lx1 + lx2 + lx3 + lx4

    def _get_compare_price(self, min, PrimeYield):
        # base_price 1550
        if min == 4:
            bonus = 1550 + 180
            return bonus
        elif min == 3:
            bonus = 1550 + 120
            return bonus
        elif min == 2:
            bonus = 1550 + 60
            return bonus
        elif min == 1:
            bonus = 1550
            return bonus
        elif min == -1:
            v = PrimeYield - 63
            bonus = 1550 - v
            return bonus

    def _check_nValue(self, VolumeWeight, PrimeYield, TasteRating, BrownIntactRatio):
        return True if VolumeWeight != 0 or PrimeYield != 0 or TasteRating != 0 or BrownIntactRatio != 0 else False

    @ api.depends('CropWeight',
                  'FinalPrice',
                  'FarmerType',
                  'CropType',
                  'FarmingMethod',
                  'CropVariety_bonus',
                  'VolumeWeight',
                  'PrimeYield',
                  'TasteRating',
                  'BrownIntactRatio',
                  'FarmingAdaption',
                  'isTGAP')
    def _compute_total_price(self):
        for record in self:
            unit_tw = record.CropWeight / 60
            record.TotalPrice = unit_tw * record.FinalPrice

    def unlink_archiveItem(self):
        self.PriceState = 'done'
        self.stage_id = self._done_stage()

    def write(self, vals):
        key = 'archived_id'
        if key in vals:
            archivedId = vals[key]
            if archivedId == 0:
                self.PriceState = 'done'
                self.stage_id = self._done_stage()
            else:
                self.PriceState = 'archived'
                self.stage_id = self._archived_stage()
        return super(Crop, self).write(vals)

    def _get_seqNumber(self):
        url = "http://ec2-34-215-20-244.us-west-2.compute.amazonaws.com:58809/api/Record"

        data = {"CropStatus": ""}
        response = requests.post(url, json=data)
        # _logger.info(response.json().get('SeqNumber'))
        return response.json().get('SeqNumber')

    @api.model
    def create(self, fields):
        _logger.info(f"this write is {fields}")
        fields['SeqNumber'] = self._get_seqNumber()
        return super(Crop, self).create(fields)

    # @api.model
    # def default_get(self, fields):
    #     res = super(Crop, self).default_get(fields)
    #     return res
