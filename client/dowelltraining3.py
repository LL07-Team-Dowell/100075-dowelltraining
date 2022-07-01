import json
import requests

#url = 'http://127.0.0.1:8000/dowell_training_api/dowelltraining3/'
url = 'https://100075.pythonanywhere.com/dowell_training_api/dowelltraining3/'

def dowelltraining3(db_name, collection_name,field_name,time_period):
    #("Dowell", "research") - sample data
    data={
        "db_name":db_name,
        "collection_name":collection_name,
        "field_name":field_name,
        "time_period":time_period,
        }

    headers = {'content-type': 'application/json'}
    response = requests.post(url, json =data,headers=headers)
    return response.text
