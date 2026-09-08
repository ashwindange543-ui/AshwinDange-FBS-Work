li = [10 , 15 , 20 , 25 , 30 , 35 , 40]
even = []
odd = []

for i in range(len(li)):
    if li[i] % 2 == 0:
        even += [li[i]]
    else:
        odd += [li[i]]

print("Even list" , even)
print("Odd list" , odd)