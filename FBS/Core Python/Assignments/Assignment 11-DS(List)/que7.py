li1 = [10, 20, 30, 40, 50]
li2 = [30, 40, 50, 60, 70]

intersection = []

for i in range(len(li1)):
    if li1[i] in li2:
        intersection = intersection + [li1[i]]

print("Intersection =", intersection)