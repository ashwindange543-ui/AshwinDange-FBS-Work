for i in range(1,6):
    for j in range(1,i+1):
        print(" " , end =" ")
    for j in range(1,7-i):
        print(chr(64+i), end =" ")
    print()