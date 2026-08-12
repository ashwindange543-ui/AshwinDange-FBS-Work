num = int(input("Enter a 3-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

print("Sum =", a + b + c)