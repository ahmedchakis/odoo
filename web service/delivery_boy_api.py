url = 'http://192.168.1.163:8069'
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
    [[97],{'delivery_boy_partner_id': False}])

#weight=models.execute_kw(db, uid, password, 'product.template', 'name', [[3]])
#print(weight)

#models.execute_kw(db, uid, password, 'res.partner', 'write', [[56], {'name': "Newer partner"}])
# get record name after having changed it
#m=models.execute_kw(db, uid, password, 'delivery.boy.pickings', 'write', [5], {'fields': ['name', 'weight']})
m=models.execute_kw(db, uid, password, 'delivery.boy.pickings', 'write', ['read'], {'raise_exception': False})
#m=models.execute_kw(db, uid, password, 'product.template', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
print(m)


