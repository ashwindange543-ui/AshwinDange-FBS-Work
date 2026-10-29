def outer():
    a="Virat"
    def innerFun():
        print(a)
    return innerFun
x=outer()
x()
