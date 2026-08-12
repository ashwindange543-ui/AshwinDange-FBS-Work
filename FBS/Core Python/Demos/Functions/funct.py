def fun1():
    print("I am good in Java..!")

fun1()
# step 1 function call-->
# step 2 function definition
#1. without parameter without return value
def add():
    no1=int(input("Enter number 1:"))
    no2=int(input("Enter number 2:"))
    print(f"Addition = {no1+no2}.")

add()
print("I am using function")
add()
print("function used kar raha hu")

#2. with parameter without return value
def add(no1,no2):
    print("Addition ={no1+no2}")
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
add(a,b)


