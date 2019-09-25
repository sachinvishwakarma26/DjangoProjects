import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
# def get_resources(id=None):
#     data={}
#     if id is not None:
#         data={
#         'id':id
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resources()
# def create_resource():
#     new_emp={
#     'eno':300,
#     'ename':'Kareena',
#     'esal':3000,
#     'eaddr':'Hyderabad',
#     }
#     r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(r.status_code)
#     # print(r.text)
#     print(r.json())
# create_resource()
def update_resource(id):
    new_data={
    'id':id,
    # 'eno':700,
    'ename':'Ravi Kumar K',
    'esal':15001,
    # 'eaddr':'Hyd'

    }
    r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(r.status_code)
    # print(r.text)
    print(r.json())
update_resource(3)
# def delete_resource(id):
#     data={
#     'id':id,
#     }
#     r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(r.status_code)
#     # print(r.text)
#     print(r.json())
# delete_resource(5)
