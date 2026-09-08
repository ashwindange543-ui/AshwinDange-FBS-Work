li = [10 , 20 , 10 , 30 , 20 , 40]
newli = []

for i in range(len(li)):
    found = False

    for j in range(len(newli)):
        if li[i] == newli[j]:
            found = True

    if found == False:
        newli += [li[i]]

print("List after removing duplicates =", newli)