s = input("Enter a string: ")

new = ""

for i in range(len(s)):
    if s[i] == ' ':
        new = new + '-'
    else:
        new = new + s[i]

print("New String =", new)
