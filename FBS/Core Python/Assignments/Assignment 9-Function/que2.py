def armstrong(num, original, n):
    if num == 0:
        return 0

    digit = num % 10
    return digit ** n + armstrong(num // 10, original, n)


num = int(input("Enter number: "))
n = len(str(num))

if armstrong(num, num, n) == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")