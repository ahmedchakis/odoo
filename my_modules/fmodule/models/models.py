# -*- coding: utf-8 -*-

from odoo import models, fields


class fmodule(models.Model):
    _inherit='res.users'

    isdeliveryboy=fields.Boolean('Is A delivery boy',required=True)

