from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django import template
import sys

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
