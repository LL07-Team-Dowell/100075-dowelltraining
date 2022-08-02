from django.urls import path

from dowelltraining.views import connection_function, population_function , get_event_id ,  Dowelltraining_main , event_creation

urlpatterns =[
 
    path('connection/',connection_function, name= 'connection'),
    path('population/',population_function, name= 'population'),
     path('Home/', Dowelltraining_main, name= 'Home'),
     path('get_event_id/', get_event_id , name= 'get_event_id'),
          path('event_creation/', event_creation, name = 'event_creation'),


]