import requests
import pprint
import json

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'

user_id = 4
response = requests.get(f'{BASE_URL_PETSTORE}/user/{user_id}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint(response.json())

data = {'name': 'Leonard'}
response = requests.post(f'{BASE_URL_PETSTORE}/user', json=data)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
dict_text = json.loads(response.text)
user_id = dict_text['message']

response = requests.delete(f'{BASE_URL_PETSTORE}/user/{user_id}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

response = requests.get(f'{BASE_URL_PETSTORE}/user/{user_id}')
pprint.pprint(f'GET {user_id}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

updated_user_data = {
    'id': 2,
    'username': 'Bob',
    'firstName': 'Bob',
    'lastName': 'Bobino',
    'email': 'Bob@rambler.com',
    'phone': '88005553535'
}
response = requests.put(f'{BASE_URL_PETSTORE}/user/1', json=updated_user_data)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

order_id = 2
response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{order_id}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint(response.json())

data = {'status': 'placed'}
response = requests.post(f'{BASE_URL_PETSTORE}/store/order/{order_id}', json=data)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)

response = requests.delete(f'{BASE_URL_PETSTORE}/store/order/{order_id}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{order_id}')
pprint.pprint(f'GET {order_id}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

updated_order_data = {
    "id": 3,
    "petId": 2,
    "quantity": 0,
    "shipDate": "2200-02-03T12:35:20.885+0000",
    "status": "placed"
}
response = requests.put(f'{BASE_URL_PETSTORE}/store/order/{order_id}', json=updated_order_data)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
