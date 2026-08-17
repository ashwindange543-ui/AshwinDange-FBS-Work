#default argument
def greet(name,msg="hi"):
    print(f'{msg} {name}')

greet("sachine")

#keyword argument
def greet(name,msg):
    print(f'{msg} {name}')

greet(msg="hello" , name="sachine")

#variable length argument
def greet(name,msg):
    print(f'{msg} {name}')

greet(msg="hello" , name="sachine")
def add(*a):
    sum=0
    for i in a:
        sum+=i
    print(sum)

add(1,2,3,4,5)

#keyword variable length argument
def greet(**kwargs):
    print(kwargs)
    print(f'{kwargs["msg"]} {kwargs["name"]}')
greet(msg="hello" , name="sachine")



