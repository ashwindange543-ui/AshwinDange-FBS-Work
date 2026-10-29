def infinite():
    i = 1
    while(True):
        yield i
        i +=1
res = infinite()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

#for i in res:
#    print(i)

