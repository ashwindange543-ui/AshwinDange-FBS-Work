s = input("Enter a string: ")

words = s.split()

for i in range(len(words)):

    found = False

    for j in range(i):
        if words[i] == words[j]:
            found = True

    if found == False:
        count = 0

        for j in range(len(words)):
            if words[i] == words[j]:
                count = count + 1

        print(words[i], "=", count)