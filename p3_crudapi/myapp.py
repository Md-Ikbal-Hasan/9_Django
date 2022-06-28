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
    r = requests.get(url=URL , data = json_data)
    data = r.json()
    print("data=>  " , data)


get_data()




# for post/ create data.................
def post_data():
    data = {'name': 'Md Sattar' , 'roll': 107 , 'city':'Thakurgaon'}

    json_data =json.dumps(data)
    r = requests.post(url=URL , data = json_data)
    data = r.json()
    print(data)

# post_data()





# for update data.................
def update_data():
    data = { 'id': 3  ,'name': 'Tamima' , 'city':'Cumilla'}

    json_data =json.dumps(data)
    r = requests.put(url=URL , data = json_data)
    data = r.json()
    print(data)


# update_data()





# for delete data.................
def delete_data():
    data = { 'id': 6}

    json_data =json.dumps(data)
    r = requests.delete(url=URL , data = json_data)
    data = r.json()
    print(data)


# delete_data()





