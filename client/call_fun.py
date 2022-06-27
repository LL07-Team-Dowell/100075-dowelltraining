from api import dowellapi

def call_fun(name,lastname):
    NewObjectID=dowellapi(name,lastname)
    return NewObjectID

print(call_fun("manish","dash"))
