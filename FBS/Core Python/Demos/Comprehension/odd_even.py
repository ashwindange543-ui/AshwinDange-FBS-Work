li = [7,9,11,2,4,15,10,20]
newli = []
for i in li:
    if i % 2 == 0:
        newli.append("even")
    else:
        newli.append("odd")
print(newli)

li = [7,9,11,2,4,15,10,20]
newli = ["even" if i % 2 == 0 else "odd" for i in li]
print(newli)