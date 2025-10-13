def outer(x):
    def inner(y):
        print("inner function Addition : ",x + y)
    inner(5)                 # you have to call inner function after function ends
    #print("outer function",x)
outer(5)

# print("Here is main variable :",x)