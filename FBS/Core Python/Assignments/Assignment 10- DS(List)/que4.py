li = [10 , 20 , 30 , 40 , 50]

i = 0
j = len(li) - 1
while i < j:
    li[i], li[j] = li[j], li[i]
    i += 1
    j -= 1

print("Reversed List =", li)