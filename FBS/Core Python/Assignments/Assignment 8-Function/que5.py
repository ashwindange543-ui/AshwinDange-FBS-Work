def prime_sum(n):
    sum = 0

    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            sum += num

    return sum

n = int(input("Enter n: "))

print("Sum of prime numbers =", prime_sum(n))