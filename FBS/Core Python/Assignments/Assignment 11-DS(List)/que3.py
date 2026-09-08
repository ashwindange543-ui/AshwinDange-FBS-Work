li = [[1, 30], [2, 10], [3, 20], [4, 15]]

for i in range(len(li)):
    for j in range(len(li) - 1):
        if li[j][1] > li[j + 1][1]:
            li[j], li[j + 1] = li[j + 1], li[j]

print(li)