# 接口
import json
import requests
import os
import base64   
import sys

payload = {"teamid": 50,
         "token": "cb454862-4dc0-4258-8a08-833343b3826b"}
data_json = json.dumps(payload)
r = requests.post('http://47.102.118.1:8089/api/challenge/record/29',data=data_json)
#print (r.content)
data = r.content
missing_padding = 4 - len(data) % 4
if missing_padding:
        data += b'=' * missing_padding
img = base64.b64decode(data)
file = open('test.jpg','wb') 
file.write(img)
file.close()
