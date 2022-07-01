
from dowelltraining3 import dowelltraining3

def call_fun(db_name, collection_name,field_name,time_period):
    NewObjectID=dowelltraining3(db_name, collection_name,field_name,time_period)
    return NewObjectID

print(call_fun('hr_hiring','dowelltraining',  ['full_name'], 'life_time'))
