starting=int(input("enter the number : "))

ending=int(input("enter the number : "))

for i in range(starting,ending,2):
    if i %2!=0:
         print(i)