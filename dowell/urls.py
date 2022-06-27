from django.urls import path

from dowell.views import dowelltraining1 

urlpatterns =[
    path('dowelltraining1/',dowelltraining1, name= 'call_dowelltraining1'),
]