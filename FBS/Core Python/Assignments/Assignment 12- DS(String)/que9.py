s = input("Enter a string: ")

characters = 0
words = 0

for i in range(len(s)):
    if s[i] != ' ':
        characters = characters + 1

        if i == 0 or s[i - 1] == ' ':
            words = words + 1

print("Number of Words =", words)
print("Number of Characters =", characters)