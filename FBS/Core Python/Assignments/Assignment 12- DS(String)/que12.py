s = input("Enter a string: ")

count = 0

for i in range(len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
        count = count + 1

print("Lowercase Characters =", count)