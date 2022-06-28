import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name' : 'Raj',
    'roll' : "107",
    'city' : 'Noakhali'
}

json_data = json.dumps(data)  # python dictionary to JSON data
r = requests.post(url=URL,data=json_data)

data  = r.json()
print("Data =>   ",data)