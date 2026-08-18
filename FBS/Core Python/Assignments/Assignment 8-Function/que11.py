def Armstrong(num):
    original = num
    sum = 0
    n = len(str(num))

    while num > 0:
        digit = num % 10
        sum += digit ** n
        num //= 10

    return original == sum

num = int(input("Enter number: "))

if Armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")