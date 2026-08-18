# a. Sum of Series 1 + 2 + 3 + ... + n
def sum_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input("Enter n: "))

print("Sum =", sum_series(n))


# b. Sum of Series 1! + 2! + 3! + ... + n!
def factorial_series(n):
    sum = 0
    fact = 1

    for i in range(1, n + 1):
        fact *= i
        sum += fact

    return sum

n = int(input("Enter n: "))

print("Sum =", factorial_series(n))


# c. Sum of Series 1^1 + 2^2 + 3^3 + ... + n^n
def power_series(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i ** i

    return sum

n = int(input("Enter n: "))

print("Sum =", power_series(n))