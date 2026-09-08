li = ["apple", "hi", "banana", "cat", "a"]

for i in range(len(li)):
    for j in range(len(li) - 1):
        if len(li[j]) > len(li[j + 1]):
            li[j], li[j + 1] = li[j + 1], li[j]

print(li)