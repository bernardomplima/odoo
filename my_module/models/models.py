from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    @api.constrains('product_qty', 'bom_id')
    def _check_bom_multiple(self):
        for record in self:
            if record.bom_id and record.bom_id.product_rounding:
                multiple = record.bom_id.product_rounding
                if multiple > 0 and record.product_qty % multiple != 0:
                    raise ValidationError(
                        f"A quantidade a produzir ({record.product_qty}) "
                        f"deve ser múltipla de {multiple} definido na Lista de Materiais."
                    )