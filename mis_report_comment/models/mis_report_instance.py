# Copyright 2021 Marçal Isern <marsal.isern@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api, fields
import json
from datetime import datetime


class MisReportInstance(models.Model):
    _inherit = "mis.report.instance"

    notes =  fields.Html(string='Notes')
    