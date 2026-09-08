li1 = [30, 10, 50]
li2 = [20, 40, 60]

newli = li1 + li2

for i in range(len(newli)):
    for j in range(len(newli) - 1):
        if newli[j] > newli[j + 1]:
            newli[j], newli[j + 1] = newli[j + 1], newli[j]

print("Sorted List =", newli)