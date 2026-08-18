def digit_sum(num):
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10

    return sum

num = int(input("Enter number: "))

print("Sum of digits =", digit_sum(num))