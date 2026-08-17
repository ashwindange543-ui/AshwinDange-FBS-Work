def separate(n):
    if n == 0:
        return
    separate(n // 10)
    print(n % 10)

#num = 12345
num = int(input("Enter a number: "))
separate(num)