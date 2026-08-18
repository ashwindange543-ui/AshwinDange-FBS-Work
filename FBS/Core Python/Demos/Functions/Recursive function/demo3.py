def printNum(n):
    if(n == 0):      #Base Case
        return
    print(n)
    printNum(n-1)     #recursive call

num = int(input("Enter a number: "))
#printNum(5)
printNum(num)