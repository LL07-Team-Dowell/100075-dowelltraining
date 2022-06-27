from django.urls import path

from dowell.views import api_call 

urlpatterns =[
    path('api_call/',api_call, name= 'api_call'),
]