import requests
import os
import base64
import json

from requests.api import head

fileDir = './localImage/'
fileName = 'IMG_2747.png'


with open(fileDir+ fileName, "rb") as f:
    json_data = {}
    bynary = base64.b64encode(f.read()).decode('utf-8')
    json_data['img_file'] = 'https://res.cloudinary.com/dagcggcea/image/upload/v1616267892/blue_output_sgdmec.png'
    json_data['aa'] = '123'
    headers = {}
    headers["Content-Type"] = "application/json"
    to_js = json.dumps(json_data)
    #requests.get('http://127.0.0.1:5000/', headers=headers)
    res = requests.post('http://localhost:5000/load', data=to_js, headers=headers)
    print(res.json(), "res")