
s = input("Enter a string: ")

count = sum(1 for ch in s if ch == ' ')

print("Spaces:", count)
