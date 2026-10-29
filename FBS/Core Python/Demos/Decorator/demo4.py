# Our function is objectb of function class 
# We can started the function in variable 
#def demo():
#    print("I am in demo")
#x=demo
## demo()
# x()
#def demo(a):
#    a()

#we can pass a function as an parameter to another function
#def fun():
#    print("I am in tested function")
#demo(fun)

# return one function from other function 
def outerfun():
    print("I am outer")
    def innerfun():
        print("I am inner function")
    return innerfun 
    #return 10
result=outerfun()
result()