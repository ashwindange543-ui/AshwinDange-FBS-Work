li = [30, 80, 20, 90, 50]

for i in range(len(li)):
    for j in range(len(li) - 1):
        if li[j] > li[j + 1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print("Second Largest =", li[len(li) - 2])