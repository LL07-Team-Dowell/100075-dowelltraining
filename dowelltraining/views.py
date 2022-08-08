from contextlib import ContextDecorator
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django import template

import time
import string
import sys
import json
import requests
import pprint
#dowell event_id
from datetime import datetime

#serializers
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

from dowell.models import Population
from dowell.serializers import PopulationFunctionSerializer
from rest_framework.decorators import api_view

def Dowelltraining_main(request):

    return render(request , 'Dowelltraining_home.html')

def event_creation(request):
    
    
 return render(request , 'event_creation.html' )

def get_event_id(request):
    global event_id
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
    event_id = r.text
    context = {'id':event_id}
    return render(request, 'event_creation.html', context )
    
    

#convert function to api


@csrf_exempt
def connection_function(request):
 global connection_id
 context = {'id':event_id }

 if (request.method=="POST"):
    
        Name = request.POST['data1']
        LastName= request.POST['data2']
        get_event_id= request.POST['data3']
        fullName = f"Your name is {Name} {LastName}"
        print(fullName)
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
                "eventId" : get_event_id,
                "full_name": fullName
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
       
        # return render(request,'connection.html', response1) 

        # return JsonResponse(response1)
        connection_id = response
        # print(connection_id)
        return HttpResponse(connection_id)
 return render(request , 'connection.html' , context )



@csrf_exempt
def population_function(request):
    r_out = connection_id.json()
    current_insertionid=r_out['inserted_id']
    if (request.method=="POST"):
        db_name = request.POST['data1']
        collection_name=  request.POST['data2']
        field_name = request.POST['data3']
        time_period=  request.POST['data4']
        field_name = list(str.split(field_name))
        def targeted_population(database, collection, fields, period):
            url = 'http://100032.pythonanywhere.com/api/targeted_population/'
            database_details = {
                'database_name': 'mongodb',
                'collection': collection,
                'database': database,
                'fields': fields
                }
            number_of_variables = -1

            time_input = {
                'column_name': 'Date',
                'split': 'week',
                'period': period,
                'start_point': '2021/01/08',
                'end_point': '2021/01/25',
                }

            stage_input_list = [
                ]

    
            distribution_input={
                'normal': 1,
                'poisson':0,
                'binomial':0,
                'bernoulli':0
                }
            request_data={
                'database_details': database_details,
                'distribution_input': distribution_input,
                'number_of_variable':number_of_variables,
                'stages':stage_input_list,
                'time_input':time_input,
                }
            headers = {'content-type': 'application/json'}

            response = requests.post(url, json=request_data,headers=headers)
            res= json.loads(response.text)
            return res

        
        response = targeted_population(db_name,collection_name,field_name,time_period)
        # print(response)
        for userdata in response['normal']['data'][0]:
         if userdata["_id"] == current_insertionid:
            current_userdatavalue = userdata
        current_userdata = json.dumps(current_userdatavalue) 
        return HttpResponse(current_userdata)
        
        # return JsonResponse ({"Data fetched using dowellpopulation function":response})
    return render(request , 'population.html')
    
 


