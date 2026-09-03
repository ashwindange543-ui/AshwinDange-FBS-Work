li = [2 , 7 , 9 , 1 , 3 , 5 , 2]

sum = 0
for ind in range(0, len(li), 2):
    sum += li[ind]
print("Sum of alternate numbers:", sum)