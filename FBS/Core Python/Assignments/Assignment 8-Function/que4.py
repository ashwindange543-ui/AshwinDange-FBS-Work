def odd_sum(n):
    sum = 0

    for i in range(1, n + 1, 2):
        sum += i

    return sum

n = int(input("Enter n: "))

print("Sum of odd numbers =", odd_sum(n))