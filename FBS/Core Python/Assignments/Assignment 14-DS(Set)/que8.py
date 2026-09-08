li = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in li:

    key = ""

    for ch in word:
        key = key + ch

    # Sort characters manually
    key = list(key)

    for i in range(len(key)):
        for j in range(len(key) - 1):
            if key[j] > key[j + 1]:
                key[j], key[j + 1] = key[j + 1], key[j]

    key = "".join(key)

    if key not in groups:
        groups[key] = []

    groups[key] = groups[key] + [word]

print(groups)