
"""
This is totally separate application from django. Its independent . Using django
drf we have received data from http://127.0.0.1:8000/stuinfo/


"""

import requests

URL = 'http://127.0.0.1:8000/stuinfo/'

r = requests.get(url=URL)
data  =r.json()
print("data=> " , data)