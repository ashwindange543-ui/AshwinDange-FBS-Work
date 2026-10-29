# 1. For memory optimization 
# 2. Generating values according to user requirement
# 3. Use yield keyword
# 4. Maintain state of function (maintainm stack frame) of function 
# 5. Iterate upcoming value using next iterable

def generateValues(n):
    for i in range(1 , n+1):
        yield i
        return i

res = generateValues(10)
#print(res)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

#for ele in res:
#    print(ele)