li = [10 , 20 , 3 , 7 , 9 , 1]

min = li[0]

for ind in range(1, len(li)):
    if(li[ind] < min):
        min = li[ind]

print("Minimum:",min)