li = [10 , 20 , 30 , 40]
newli = []
for i in range(len(li)):
    newli += [li[i]]
print("Original list =", li)
print("Duplicates list =", newli)

print(li is newli)