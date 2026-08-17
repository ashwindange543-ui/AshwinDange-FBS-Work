# Sinple recursive function
def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n - 1)

print("Sum =", sum_num(10))


# Using for loop
def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n - 1)

sum = 0

for i in range(1, 11):
    sum += 1

print("Sum =", sum_num(10))


# Using while loop
def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n - 1)

i = 1

while i <= 10:
    i += 1

print("Sum =", sum_num(10))