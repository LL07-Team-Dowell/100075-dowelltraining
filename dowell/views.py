from django.http import HttpResponse, JsonResponse
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

#serializers
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

from .models import Population
from .serializers import PopulationFunctionSerializer
from rest_framework.decorators import api_view


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
        #return JsonResponse ({"Answer":fullName})
        return HttpResponse(fullName)

@csrf_exempt
def dowellweb(request):
    if (request.method=="POST"):
        Name = request.POST['data1']
        LastName= request.POST['data2']
        fullName = f"Your name is {Name} {LastName}"
        return JsonResponse ({"Answer":fullName})
        #return HttpResponse(fullName)

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
                "eventId" : get_event_id(),
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
        print(response.text)
        #return JsonResponse ({"Data inserted sucessfully using dowellcoonection function":response.text})
        return HttpResponse(response.text)

        #return JsonResponse ({"Answer":fullName})
#dowellpopulation function to fetch data
@csrf_exempt
def dowelltraining3(request):
    if (request.method=="POST"):
        request_data=json.loads(request.body)
        print(request_data)
        db_name = request_data['db_name']
        collection_name= request_data['collection_name']
        field_name=request_data['field_name']
        time_period=request_data['time_period']
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

            return response.text
        response = targeted_population(db_name,collection_name,field_name,time_period)
        print(response)
        #return JsonResponse ({"Data fetched using dowellpopulation function":response})
        return HttpResponse(response)

@csrf_exempt
@api_view(['POST'])
def home(request):
    serializer = PopulationFunctionSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_name(request):
    jobs = Population.objects.all()
    serializer = PopulationFunctionSerializer(jobs, many=True)
    return Response(serializer.data)

