var = 5
def outer():
    c = 6
    def inner():
        nonlocal c  # we can access outer method variable using nonlocal variable
        d = 7
        c = d
        print("inner func var --> ",d)
    inner()
    print("outer func var --> ",c)
outer()
print("Global func var -->",var)

