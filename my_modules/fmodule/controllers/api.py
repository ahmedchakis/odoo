from odoo import http

class TestApi(http.Controller):
    @http.route('/api',auth='public',website=False)
    def hello(self,**kw):
        return 'Hello'
