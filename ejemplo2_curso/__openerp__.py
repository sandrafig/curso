# -*- coding: utf-8 -*-
# © <2016> <Alumnx>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "ejemplo2_curso",
    "summary": "Pestaña Ofertas en Pedido de venta",
    "version": "1.0",
    "author": "Alumnx",
    "website": "http://osig.webs.uvigo.es",
    "category": "Sale",
    "license": "AGPL-3",
    "depends": [
        "base",
        "sale",
        "report",
    ],
    "data": [
        'views/ofertas_view.xml',
        'views/ofertas_report.xml',
        'report/ofertas.xml',
    ],
    "installable": True
}