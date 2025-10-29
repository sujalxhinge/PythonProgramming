#Kwargs in python
def kwargs(**kargs):
    for key, value in kargs.items():
        print(key, value)

Dict_1={"parameter_1 ": 50,
"parameter_2": 100
}

kwargs(Dict_1 = Dict_1)

