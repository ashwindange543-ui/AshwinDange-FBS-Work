li = [10, 15, 20, 25, 30, 35, 40]

newli = []

for i in range(len(li)):
    if li[i] % 2 != 0:
        newli += [li[i]]

print("List after removing even numbers =", newli)