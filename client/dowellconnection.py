import json
import requests
import pprint

url = "http://100002.pythonanywhere.com/" 
#searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"
payload = json.dumps({
    "cluster": "hr_hiring",
    "database": "hr_hiring",
    "collection": "dowelltraining",
    "document": "dowelltraining",
    "team_member_ID": "1000554",
    "function_ID": "ABCDE",
    "command": "insert",
    "field": {
        "fullname": "Your name is uxliving lab"
        },
    "update_field": {
        "order_nos": 21
        },
    "platform": "bangalore"
    })
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
