def palindrome(num):
    rev = 0
    temp = num

    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    if temp == rev:
        return True
    else:
        return False

num = int(input("Enter number: "))
print(palindrome(num))