li = [10,2,3,4,7,11,33]
newli = []
for i in li:
    if i % 2 != 0:
        newli.append(i)
print(newli)

li = [10,2,3,4,7,11,33]
newli = [i for i in li if i % 2 != 0]
print(newli)
