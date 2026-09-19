n = int(input("Enter n: "))

sum = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (i / fact)

print("Sum =", sum)