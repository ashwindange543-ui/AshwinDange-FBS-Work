def chkEvenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

data = [1 ,2 ,3 , 5 , 6, 7 , 8 , 9 , 10]

#res = map(lambda num : num * num, data)
res = list(map(chkEvenOdd, data))

print(res)