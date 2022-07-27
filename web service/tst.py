import base64
import json
import requests

# Authentication
r = requests.get('http://192.168.1.153:8069/api/auth/get_tokens?username=admin&password=111')
print(r.json())
access_token = r.json()['access_token']




#print(access_token)

# GET - Read record
r = requests.get(
    'http://192.168.1.153:8069/api/login',
    headers = {'Access-token': access_token,'db':'odoo15','login':'admin','password':'111'})
print(r.json())


r = requests.get(
    'http://192.168.1.153:8069/api/stock.picking',
    headers = {'Access-Token': access_token})
    #return r.json()

url = "https://www.googleapis.com/books/v1/volumes?q=1";
response = requests.get(url)
json_data = response.json()
loaded_json = json.dumps(json_data)
book = json_data['items'][0]
image_url = book["volumeInfo"]['imageLinks']['smallThumbnail'] # here contains image url such as thumbnail
img = base64.b64encode(requests.get(image_url).content)
print(img)

'''# PUT - Update record
r = requests.put(
    'http://localhost:8069/res.partner/26?name=Tom Lenz&city=New York',
    headers = {'Access-Token': access_token})
print(r)'''