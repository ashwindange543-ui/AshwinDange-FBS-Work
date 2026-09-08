s = input("Enter a string: ")

new = ""

for i in range(len(s)):
    if s[i] == 'a':
        new += '$'
    else:
        new += s[i]

print("New String =", new)
