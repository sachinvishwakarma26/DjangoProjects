import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id=None):
    data={}
    if id is not None:
        data={'id':id}
    r=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(r.status_code)
    print(r.json())
    print(r.text)
def create_resource():
    newemp={
    'eno':700,
    'ename':'Ravi',
    'esal':40000,
    'eaddr':'Hyderabad'
    }
    r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(newemp))
    print(r.status_code)
    # print(r.text)
    print(r.json())

def update_resource(id):
    new_data={
    'id':id,
    'esal':20000
    }
    r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(r.status_code)
    # print(r.text)
    print(r.json())

def delete_resource(id):
    data={
    'id':id
    }
    r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(r.status_code)
    # print(r.text)
    print(r.json())
delete_resource(150)
