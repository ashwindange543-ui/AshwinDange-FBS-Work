# a. Sum of factorial series (1! + 2! + 3! +..+ n!)

n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    fact = 1

    for j in range(1, i + 1):
        fact = fact * j

    sum = sum + fact

print("Sum =", sum)

# b. Series (N + N**2 + N**3 +...+ N**N )

n = int(input("Enter value of N: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + n ** i

print("Sum =", sum)

# c. Geometric Series(Comman Ratio = 2)
#(1 + 2 + 4 + 8 + ...)

n = int(input("Enter number of terms: "))

sum = 0
term = 1

for i in range(n):
    sum = sum + term
    term = term * 2

print("Sum =", sum)

# d. Series (a + a**2/2 + a**3/3 +...+ a**10/10)

a = int(input("Enter value of a: "))

sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print("Sum =", sum)

# e. Series (x - x**2/3 + x**3/5 - x**4/7 +... (n terms))

x = int(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0
sign = 1
odd = 1

for i in range(1, n + 1):
    sum = sum + sign * (x ** i) / odd
    sign = -sign
    odd = odd + 2

print("Sum =", sum)