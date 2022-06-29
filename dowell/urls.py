from django.urls import path

from dowell.views import dowelltraining1 ,dowelltraining2

urlpatterns =[
    path('dowelltraining1/',dowelltraining1, name= 'call_dowelltraining1'),
    path('dowelltraining2/',dowelltraining2, name= 'call_dowelltraining2'),
    
]