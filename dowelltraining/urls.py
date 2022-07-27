from django.urls import path

from dowelltraining.views import dowelltraining2web, dowelltraining3web

urlpatterns =[

    path('dowelltraining2web/',dowelltraining2web, name= 'dowelltraining2web'),
    path('dowelltraining3web/',dowelltraining3web, name= 'dowelltraining3web'),

]