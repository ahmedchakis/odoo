url = 'http://localhost:8069'
db = 'odoo15'
username = 'admin'
password = '111'
import xmlrpc.client
import requests

common = xmlrpc.client.ServerProxy('%s/xmlrpc/2/common' % url)
version = common.version()
print("details...", version) 
uid=common.authenticate(db,username,password,{})
print("UID",uid)
models=xmlrpc.client.ServerProxy('%s/xmlrpc/2/object' % url)
from flask import request
from flask import Flask
from flask import render_template
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt=Bcrypt(app)



@app.route('/recieve_data')
def get_id():
   the_id = request.args.get('button_id')
   return the_id

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('./filename.html')



#select all deliveries assigned to the delivery boy
@app.route('/delivery_orders')
def delivery_orders():
    r = requests.get('http://localhost:8069/api/auth/get_tokens?username=admin&password=111')
    print(r.json())
    access_token = r.json()['access_token']
    #print(access_token)
    
    # GET - Read record
    r = requests.get(
    'http://localhost:8069/api/delivery.boy.pickings',
    headers = {'Access-Token': access_token})
    return str(r.json()['results']).replace("'", '"')   
    #picking=models.execute_kw(db, uid, password,
    #'stock.picking', 'search_read',
    #[[]],{'fields': ['display_name','state']})
    #print("picking...",picking)
    #return str(picking)





@app.route('/delivery_orders/<id>',methods=['GET','PUT'])
def delivery_orders_id(id):
    
    if request.method=="GET":  
        #display details of the delivery 
        picking=models.execute_kw(db, uid, password,
        'stock.picking', 'search_read',
        [[['id','=',id]]])
        print("picking...",picking)
        return str(picking)
    else:
        #set delivery to done (the customer has received his delivery)
        models.execute_kw(db, uid, password, 'stock.picking', 'write', [[int(id)], {'state': "done"}])
        return 'state of delivery with id:%s is set to done' %id

#the delivey boy sets himself online or offline
@app.route('/connectivity/<id>/<status>',methods=['PUT'])
def set_status(id,status):
    if request.method=="PUT":
        if status=='online':
            models.execute_kw(db, uid, password, 'res.users', 'write', [[int(id)], {'active': True}])
        else:
            models.execute_kw(db, uid, password, 'res.users', 'write', [[int(id)], {'active': False}])
        return 'you are now %s ' %status

@app.route('/login',methods=['POST'])
def login():
    login=request.form['login']
    password_=request.form['password']

    res=models.execute_kw(db, uid, password,
    'user.test', 'search_read'
    ,[[['login','=',login]]])


    return str(res)
        
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

