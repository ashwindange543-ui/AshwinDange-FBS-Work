li = [30 , 10 , 50 , 20 , 40]
maximum = li[0]
minimum = li[0]
for i in range(len(li)):
    if li[i] > maximum:
        maximum = li[i]
    if li[i] < minimum:
        minimum = li[i]
print("Maximum =", maximum)
print("Minimum =", minimum)