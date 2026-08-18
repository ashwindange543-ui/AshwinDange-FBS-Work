def prime(num, i):
    if num < 2:
        return False

    if i == num:
        return True

    if num % i == 0:
        return False

    return prime(num, i + 1)


num = int(input("Enter number: "))

if prime(num, 2):
    print("Prime Number")
else:
    print("Not Prime Number")
    