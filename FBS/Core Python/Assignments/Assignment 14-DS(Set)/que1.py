set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}

result = set()

for x in set1:
    if x not in set2:
        result.add(x)

print("Elements in set1 but not in set2 =", result)