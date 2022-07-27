from .main import *
from odoo import http
from odoo.http import request
import xmlrpc.client
from odoo.exceptions import AccessDenied, AccessError
import requests
import logging
import datetime

_logger = logging.getLogger(__name__)

class ControllerREST(http.Controller):
    @http.route('/api/custom', methods=['GET'], type='http', auth='public', cors=rest_cors_value)
    def a(self, **kw):
        # get Odoo env params
        cr, uid = request.cr, request.session.uid
        # get any model as ordinary Odoo object
        odoo_model_obj = request.env(cr, uid)['res.partner']
        # make models manipulations, actions, computations etc. And if you need, fill the results dictionary
        your_custom_dict_data = {'your_vals': '...'}
        # send HTTP response
        return successful_response(status=200, dict_data=your_custom_dict_data)





    @http.route("/api/unbind/<id>", methods=["PUT"], type="http", auth="none", csrf=False)
    def api_unbind_order(self,id, **post):
        print(id)
        url = 'http://192.168.1.153:8069'
        db = 'odoo15'
        username = 'admin'
        password = '111'
        import xmlrpc.client

        common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
        version = common.version()
        print("details...", version)

        uid=common.authenticate(db,username,password,{})
        print("UID",uid)


        models=xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % url)
        picking=models.execute_kw(db, uid, password,
            'stock.picking', 'write',
            [[int(id)],{'delivery_boy_partner_id': False}])

    @http.route("/api/verify/<id>", methods=["POST"], type="http", auth="none", csrf=False)
    def api_verify(self,id, **post):
        headers = request.httprequest.headers
        code = headers.get("code")

        url = 'http://192.168.1.18:8069'
        db = 'odoo15'
        username = 'admin'
        password = '111'
        import xmlrpc.client
        common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
        uid=common.authenticate(db,username,password,{})
        models=xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % url)
        
        m=models.execute_kw(db, uid, password, 'delivery.boy.pickings', 'read', [int(id)], {'fields': ['delivery_token']})
        print(request.httprequest.data.decode())

        return json.dumps({'value':m[0]['delivery_token']==code})

    @http.route("/api/delivered_date/<id>", methods=["GET"], type="http", auth="none", csrf=False)
    def api_delivery_date(self,id, **post):
        url = 'http://192.168.1.18:8069'
        db = 'odoo15'
        username = 'admin'
        password = '111'
        import xmlrpc.client
        common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
        uid=common.authenticate(db,username,password,{})
        
        models=xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % url)
        m=models.execute_kw(db, uid, password, 'delivery.boy.pickings', 'read', [int(id)], {'fields': ['write_date']})
        print(request.httprequest.data.decode())

        return m[0]['write_date']

    @http.route("/api/show_page/<id>",methods=["GET"], type="http", auth="public", csrf=False)
    def show_page(self,id,**post):
        url = 'http://192.168.1.153:8069'
        db = 'odoo15'
        username = 'admin'
        password = '111'
        import xmlrpc.client

        common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
        uid=common.authenticate(db,username,password,{})
        print("UID",uid)


        models=xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % url)
        m=models.execute_kw(db, uid, password, 'product.template', 'read', [int(id)], {'fields': ['name', 'weight']})
        print(m)
        content= '<!DOCTYPE html><style>.card {'
        content+='  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);'
        content+='  max-width: 300px;     '    
        content+='  margin: auto;'
        content+='  text-align: center;'
        content+='  font-family: arial;'
        content+='}'
        content+='.price {'
        content+='  color: grey;'
        content+='  font-size: 22px;'
        content+='}'
        content+='.card button {'
        content+='  border: none;'
        content+='  outline: 0;'
        content+='  padding: 12px;'
        content+='  color: white;'
        content+='  background-color: #000;'
        content+='  text-align: center;'
        content+='  cursor: pointer;'
        content+='  width: 100%;'
        content+='  font-size: 18px;'
        content+='}'
        content+='.card button:hover {'
        content+='  opacity: 0.7;'
        content+='}</style><html><body><div class="card"><img src="data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO    9TXL0Y4OHwAAAABJRU5ErkJggg==" alt="Denim Jeans" style="width:100%"><h1>'+m[0]['name']+'</h1><p class="price">'+str(m[0]['weight'])+'</p><p>Some text about the jeans..</p><p><button>Add to Cart</button></p></div></body></html>'
        return content

    @http.route("/api/login", methods=["GET"], type="http", auth="none", csrf=False)
    def api_login(self, **post):


        headers = request.httprequest.headers
        db = headers.get("db")
        login = headers.get("login")
        password = headers.get("password")
        print("input from headers",db,login,password)
        try:
            request.session.authenticate(db, login, password)
        except AccessError as aee:
            return self.invalid_response("Access error", "Error: %s" % aee.name)
        except AccessDenied as ade:
            return invalid_response("Access denied", "Login, password or db invalid")
        except Exception as e:
            # Invalid database:
            info = "The database name is not valid {}".format((e))
            error = "invalid_database"
            _logger.error(info)
            return invalid_response("wrong database name", error, 403)
        uid = request.session.uid
        #url='http://localhost:8069/api/auth/get_tokens?username=%s&password=%s'%(login,password)
        url='http://localhost:8069/api/auth/get_tokens?username=admin&password=111'
        access_token = requests.get(url).json()['access_token']

        if(uid):
            return werkzeug.wrappers.Response(
            status=200,
            content_type="application/json; charset=utf-8",
            headers=[("Cache-Control", "no-store"), ("Pragma", "no-cache")],
            response=json.dumps(
                {
                    "uid": uid,
                    "user_context": request.session.get_context() if uid else {},
                    "status":request.env.user.delivery_boy_status,
                    "name":request.env.user.partner_id.name,
                    "company_id": request.env.user.company_id.id if uid else None,
                    "company_ids": request.env.user.company_ids.ids if uid else None,
                    "partner_id": request.env.user.partner_id.id,
                    "access_token": access_token,
                    "company_name": request.env.user.company_name,
                    "country": request.env.user.country_id.name,
                    "contact_address": request.env.user.contact_address,
                    "image":request.env.user.image_512,
                }
            )
        )
        else:
            return werkzeug.wrappers.Response(
            status=401,
            content_type="application/json; charset=utf-8",
            headers=[("Cache-Control", "no-store"), ("Pragma", "no-cache")],
            response=json.dumps(
                {
                    'error':'wrong credentials'
                }
            )
        )







            '''return werkzeug.wrappers.Response(
            status=200,
            content_type="application/json; charset=utf-8",
            headers=[("Cache-Control", "no-store"), ("Pragma", "no-cache")],
            response=json.dumps(
                {
                    "uid": uid,
                    "user_context": request.session.get_context() if uid else {},
                    "company_id": request.env.user.company_id.id if uid else None,
                    "company_ids": request.env.user.company_ids.ids if uid else None,
                    "partner_id": request.env.user.partner_id.id,
                    "access_token": access_token,
                    "company_name": request.env.user.company_name,
                    "country": request.env.user.country_id.name,
                    "contact_address": request.env.user.contact_address,
                }
            ),
            )'''



def invalid_response(typ, message=None, status=401):
        """Invalid Response
        This will be the return value whenever the server runs into an error
        either from the client or the server."""
        # return json.dumps({})
        return werkzeug.wrappers.Response(
            status=status,
            content_type="application/json; charset=utf-8",
            response=json.dumps(
                {"type": typ, "message": str(message) if str(message) else "wrong arguments (missing validation)",},
                
            ),
        )
        


        
