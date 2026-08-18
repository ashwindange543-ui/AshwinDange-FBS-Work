def printNum(start, end):
    if start > end :
        return

    print(start)
    printNum(start + 1, end)     # Recursive Call

start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
printNum(start , end)