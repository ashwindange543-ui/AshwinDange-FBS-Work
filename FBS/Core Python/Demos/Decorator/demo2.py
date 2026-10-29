#def fun(a):
#    print(a)
#def demo():
#    print("I am in demo")
#print(type(demo))
#a=10
#print(type(a))
#x=demo
#demo()
#x()
#fun("PRavin")

def fun(a):
    a()
def demo():
    print("I am in demo")
x=demo
fun(x)