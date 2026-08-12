x = 10 
y = 10          # Reuse - Immutable(orignal in changed value)
z = 20
# Mutable - New mmemory
#Allocated
li1 = [10 , 20]
li2 = [10 , 20]

print(id(x))         #140720669234376
print(id(y))         #140720669234376
print(x is y)        #True
print(x is z)        #False

print(id(li1))       #3088359121088
print(id(li2))       #3088359268928
print(li1 is li2)    #False
