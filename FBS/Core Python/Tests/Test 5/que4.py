li = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

d = {}

for i in li:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)