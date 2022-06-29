from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django import template
import sys
import json
import requests
import pprint
#dowell event_id
from datetime import datetime
import requests

def get_event_id():
    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    url="https://100003.pythonanywhere.com/event_creation"

    data={
        "platformcode":"FB" ,
        "citycode":"101",
        "daycode":"0",
        "dbcode":"pfm" ,
        "ip_address":"192.168.0.41",
        "login_id":"lav",
        "session_id":"new",
        "processcode":"1",
        "regional_time":time,
        "dowell_time":time,
        "location":"22446576",
        "objectcode":"1",
        "instancecode":"100051",
        "context":"afdafa ",
        "document_id":"3004",
        "rules":"some rules",
        "status":"work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour":"color value",
        "hashtags":"hash tag alue",
        "mentions":"mentions value",
        "emojis":"emojis",

    }


    r=requests.post(url,json=data)
    return r.text

#convert function to api
@csrf_exempt
def dowelltraining1(request):
    if (request.method=="POST"):
        request_data=json.loads(request.body)
        print(request_data)
        Name = request_data['name']
        LastName= request_data['lastname']
        fullName = f"Your name is {Name} {LastName}"
        return JsonResponse ({"Answer":fullName})

#dowellconnection insert data
@csrf_exempt
def dowelltraining2(request):
    if (request.method=="POST"):
        request_data=json.loads(request.body)
        print(request_data)
        Name = request_data['name']
        LastName= request_data['lastname']
        fullName = f"Your name is {Name} {LastName}"
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
                "event_id" : get_event_id(),
                "fullname": fullName
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
        return JsonResponse ({"Inserted Sucessfully":response.text})

        #return JsonResponse ({"Answer":fullName})
