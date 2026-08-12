num = int(input("Enter a 3-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

reverse = c * 100 + b * 10 + a

if(num == reverse):
    print("Palindrome")
else:
    print("Not Palindrome")