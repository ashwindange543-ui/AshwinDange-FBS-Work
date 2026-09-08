li = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(li[0])):

    ch = li[0][i]
    same = True

    for j in range(1, len(li)):
        if i >= len(li[j]) or li[j][i] != ch:
            same = False
            break

    if same == True:
        prefix = prefix + ch
    else:
        break

print("Longest Common Prefix =", prefix)