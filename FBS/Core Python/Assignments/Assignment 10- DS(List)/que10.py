li = [10, 20, 10, 30, 10, 40]

num = int(input("Enter element to remove: "))

newli = []

for i in range(len(li)):
    if li[i] != num:
        newli = newli + [li[i]]

print("List after removing =", newli)