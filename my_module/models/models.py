from odoo import models, api, _
from odoo.exceptions import ValidationError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.constrains('product_qty', 'bom_id')
    def _check_bom_multiple(self):
        for production in self:
            bom = production.bom_id
            if bom and bom.product_qty > 0:
                if production.product_qty % bom.product_qty != 0:
                    raise ValidationError(_(
                        "A quantidade a produzir (%s) deve ser um múltiplo da quantidade definida na Lista de Materiais (%s)."
                    ) % (production.product_qty, bom.product_qty))