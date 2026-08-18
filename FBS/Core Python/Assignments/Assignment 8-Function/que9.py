def palindrome(num):
    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return original == rev

num = int(input("Enter number: "))

if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")