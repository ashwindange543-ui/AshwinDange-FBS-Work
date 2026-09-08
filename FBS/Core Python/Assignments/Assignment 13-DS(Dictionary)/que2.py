d1 = {"a": 10, "b": 20}
d2 = {"c": 30, "d": 40}

d3 = {}

for key in d1:
    d3[key] = d1[key]

for key in d2:
    d3[key] = d2[key]

print("Combined Dictionary =", d3)