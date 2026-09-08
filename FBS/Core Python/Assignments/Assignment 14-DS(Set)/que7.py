set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}

missing_in_set2 = set()
missing_in_set1 = set()

for x in set1:
    if x not in set2:
        missing_in_set2.add(x)

for x in set2:
    if x not in set1:
        missing_in_set1.add(x)

print("Missing in Set2 =", missing_in_set2)
print("Missing in Set1 =", missing_in_set1)