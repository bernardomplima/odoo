from odoo import models, fields, api
from odoo.exceptions import ValidationError
import math

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    rounding = fields.Float(
        string='Múltiplo de Produção',
        default=1.0,
        help="A quantidade a produzir deve ser múltipla deste valor."
    )

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.constrains('product_qty')
    def _check_qty_rounding(self):
        for record in self:
            if record.bom_id and record.bom_id.rounding > 0:
                rounding = record.bom_id.rounding
                qty = record.product_qty
                if not math.isclose(qty % rounding, 0.0, abs_tol=1e-6):
                    raise ValidationError(
                        f"A quantidade a produzir ({qty}) deve ser múltipla de {rounding}."
                    )