import json
import requests

#url = 'http://127.0.0.1:8000/dowell_training_api/dowelltraining1/'
url = 'https://100075.pythonanywhere.com/dowell_training_api/dowelltraining1/'

def dowelltraining1(name, lastname):
    #("Dowell", "research") - sample data
    data={
        "name":name,
        "lastname":lastname,
        }

    headers = {'content-type': 'application/json'}
    response = requests.post(url, json =data,headers=headers)
    return response.text