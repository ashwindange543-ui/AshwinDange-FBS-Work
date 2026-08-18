def seperate(n):
    if(n == 0):
        return
    
    digit = n % 10
    print(digit)
    seperate(n // 10)

#num = 123456
num = int(input("Enter a number: "))
res = seperate(num)
print(res)

