s = input("Enter a string: ")

digits = 0
letters = 0

for i in range(len(s)):

    if s[i] >= '0' and s[i] <= '9':
        digits = digits + 1

    elif (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
        letters = letters + 1

print("Digits =", digits)
print("Letters =", letters)