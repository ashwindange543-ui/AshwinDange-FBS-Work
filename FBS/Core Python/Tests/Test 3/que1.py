n = int(input("Enter n: "))

count = 0
num = 2

while count < n:
    i = 2
    flag = 0

    while i < num:
        if num % i == 0:
            flag = 1
            break
        i = i + 1

    if flag == 0:
        print(num, end=" ")
        count = count + 1

    num = num + 1