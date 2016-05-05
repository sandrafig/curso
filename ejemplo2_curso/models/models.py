# -*- coding: utf-8 -*-
# © <2016> <Alumnx>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api

class OfertasCurso(models.Model):
	_name = 'ofertas.curso'

	inc_imagen = fields.Boolean(string="Incluir imagen", default=False)
	tipo_madera = fields.Selection([
		('pino', "Pino"),
		('eucalipto', "Eucalipto"),
		('otro', "Otro"),
	], default='pino', string="Tipo de madera")
	tipo_madera_otro = fields.Char(string="Especifique")
	cant_min = fields.Selection([
		('camion', "Camión completo"),
		('otro', "Otro"),
	], default='camion', string="Cantidades mínimas")
	cant_min_otro = fields.Char(default="X unidades", string="Especifique")
	calidad_madera = fuelds.Selection([
		('1', "1ª"),
		('2', "2ª"),
		('otro', "Otro"),
	], default='1', string="Calidad de la madera")
	calidad_madera_otro = fields.Char(string="Especifique")
    transporte = fields.Char(string="Inclusión del transporte", default="Sí (hasta sus instalaciones)")
    plazo_entrega = fields.Char(string="Plazo de entrega", default="X días apartir de la recepción del pedido")
    condiciones_pago = fields.Selection([
        ('acostumbrada', "Acostumbrada"),
        ('contado', "Contado"),
        ('otro', "Otro"),
    ], default='acostumbrada', string="Condiciones de pago")
    condiciones_pago_otro = fields.Char(default="A X días", string="Especifique")
    frec_entregas = fields.Selection([
        ('pedido', "Según pedidos"),
        ('otro', "Otro"),
    ], default='pedido', string="Frecuencia entregas")
    frec_entregas_otro = fields.Char(string="Especifique")

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    email = fields.Char(string="Email", related="partner_id.email")
    fax = fields.Char(string="Fax", related="partner_id.fax")
    phone = fields.Char(string="Teléfono", related="partner_id.phone")
    inc_imagen = fields.Boolean(string="Incluir imagen", default=False)
    tipo_madera = fields.Selection([
        ('pino', "Pino"),
        ('eucalipto', "Eucalipto"),
        ('otro', "Otro"),
    ], default='pino', string="Tipo de madera")
    tipo_madera_otro = fields.Char(string="Especifique")
    cant_min = fields.Selection([
        ('camion', "Camión completo"),
        ('otro', "Otro"),
    ], default='camion', string="Cantidades mínimas")
    cant_min_otro = fields.Char(default="X unidades", string="Especifique")
    calidad_madera = fields.Selection([
        ('1', "1ª"),
        ('2', "2ª"),
        ('otro', "Otro"),
    ], default='1', string="Calidad de la madera")
    calidad_madera_otro = fields.Char(string="Especifique")
    transporte = fields.Char(string="Inclusión del transporte", default="Sí (hasta sus instalaciones)")
    plazo_entrega = fields.Char(string="Plazo de entrega", default="X días apartir de la recepción del pedido")
    condiciones_pago = fields.Selection([
        ('acostumbrada', "Acostumbrada"),
        ('contado', "Contado"),
        ('otro', "Otro"),
    ], default='acostumbrada', string="Condiciones de pago")
    condiciones_pago_otro = fields.Char(default="A X días", string="Especifique")
    frec_entregas = fields.Selection([
        ('pedido', "Según pedidos"),
        ('otro', "Otro"),
    ], default='pedido', string="Frecuencia entregas")
    frec_entregas_otro = fields.Char(string="Especifique")
