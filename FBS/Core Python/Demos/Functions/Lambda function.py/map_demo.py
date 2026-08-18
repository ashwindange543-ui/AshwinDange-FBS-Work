#lambda num : num * num
data = [1 ,2 ,3 , 5 , 6, 7 , 8 , 9 , 10]

#res = map(lambda num : num * num, data)
res = list(map(lambda num : num * num, data))

print(res)