s = input("Enter a string: ")
n = int(input("Enter index: "))

new = ""

for i in range(len(s)):
    if i != n:
        new += s[i]

print("New String =", new)