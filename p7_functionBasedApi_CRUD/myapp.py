from dataclasses import dataclass
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"




# for get data from database....................
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}

    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    r = requests.get(url=URL ,headers=headers, data = json_data)
    data = r.json()
    print(data)


# get_data(2)




# for post/ create data.................
def post_data():
    data = {'name': 'ASik' , 'roll': 104 , 'city':'Noakhali'}
    headers = {'content-Type' : 'application/json'}

    json_data =json.dumps(data)
    r = requests.post(url=URL , headers=headers   , data = json_data)
    data = r.json()
    print(data)

# post_data()





# for update data.................
def update_data():
    data = { 'id': 2  ,'name': 'Mr Mubin Mia' , 'city':'Cumilla'}
    headers = {'content-Type' : 'application/json'}
    json_data =json.dumps(data)
    r = requests.put(url=URL , headers= headers, data = json_data)
    data = r.json()
    print(data)


# update_data()





# for delete data.................
def delete_data():
    data = { 'id': 4}

    json_data =json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    r = requests.delete(url=URL , headers=headers  , data = json_data)
    data = r.json()
    print(data)


delete_data()





