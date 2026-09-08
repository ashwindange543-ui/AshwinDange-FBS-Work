li = [2, 3, 4, 5]

square = []
cube = []

for i in range(len(li)):
    square += [li[i] ** 2] 
    cube += [li[i] ** 3]

print("Numbers =", li)
print("Squares =", square)
print("Cubes =", cube)