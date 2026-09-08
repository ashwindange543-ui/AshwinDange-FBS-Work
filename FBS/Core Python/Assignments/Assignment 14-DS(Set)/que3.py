li = ["cat", "dog", "cat", "bird", "dog", "cat"]

unique = set()

for word in li:
    unique.add(word)

for word in unique:
    count = 0

    for x in li:
        if word == x:
            count = count + 1

    print(word, "=", count)