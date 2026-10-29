def outer():
    print("I am in outer function")
    def innerFun():
        print("I am from inner function")
    return innerFun
x=outer()
x()