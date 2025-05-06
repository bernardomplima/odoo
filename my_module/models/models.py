from odoo import models, api
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.constrains('product_qty')
    def _check_bom_multiple(self):
        for record in self:
            bom = self.env['mrp.bom']._bom_find(product=record.product_id, company_id=record.company_id.id)
            if bom:
                base_qty = bom.product_qty or 1
                if record.product_qty % base_qty != 0:
                    raise UserError(
                        f"A quantidade da ordem de produção ({record.product_qty}) deve ser um múltiplo de {base_qty} conforme definido na Lista de Materiais (BOM)."
                    )
