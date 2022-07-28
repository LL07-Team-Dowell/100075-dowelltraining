from django.urls import path

from dowelltraining.views import connection_function, population_function

urlpatterns =[
 
    path('connection/',connection_function, name= 'connection'),
    path('population/',population_function, name= 'population'),


]