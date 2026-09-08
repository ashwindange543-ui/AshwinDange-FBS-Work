s = input("Enter a string: ")

new = s[len(s) - 1]

for i in range(1, len(s) - 1):
    new = new + s[i]

new = new + s[0]

print("New String =", new)