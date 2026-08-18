def Armstrong(num):
    temp = num
    sum = 0
    n = len(str(num))

    while num > 0:
        digit = num % 10
        sum = sum + digit ** n
        num = num // 10

    return sum == temp

data = [1 ,2 ,3 , 153 , 123 , 83 , 5 , 6, 7 , 8 , 9 , 10]

#res = map(lambda num : num * num, data)

res = list(map(lambda num: Armstrong(num *num), data))

print(res)