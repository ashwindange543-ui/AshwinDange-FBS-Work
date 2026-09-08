set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}

for x in set2:
    if x in set1:
        set1.remove(x)

print("Set1 =", set1)