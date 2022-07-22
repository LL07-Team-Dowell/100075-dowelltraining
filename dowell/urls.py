from django.urls import path

from dowell.views import dowelltraining1 ,dowelltraining2,dowelltraining3,home,get_name,dowellweb

urlpatterns =[
    path('dowelltraining1/',dowelltraining1, name= 'call_dowelltraining1'),
    path('dowelltraining2/',dowelltraining2, name= 'call_dowelltraining2'),
    path('dowelltraining3/',dowelltraining3, name= 'call_dowelltraining3'),
    path('home/',home, name= 'home'),
    path('get_name/',get_name, name= 'get_name'),
    path('dowellweb/',dowellweb,name='dowellweb'),
]