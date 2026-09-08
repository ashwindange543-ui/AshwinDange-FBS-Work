s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

count1 = 0
count2 = 0

for ch in s1:
    count1 = count1 + 1

for ch in s2:
    count2 = count2 + 1

if count1 > count2:
    print("Larger String =", s1)
elif count2 > count1:
    print("Larger String =", s2)
else:
    print("Both strings are equal")