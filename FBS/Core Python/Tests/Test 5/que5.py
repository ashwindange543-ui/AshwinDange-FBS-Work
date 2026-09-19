li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]

union = []

for i in li1:
    if i not in union:
        union.append(i)

for i in li2:
    if i not in union:
        union.append(i)

print("Union =", union)