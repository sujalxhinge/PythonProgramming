def outer():
    x = "hello"
    def inner():
        nonlocal x
        d = "hi"
        x = d
        print(x)
    inner()
    print(x)

outer()
