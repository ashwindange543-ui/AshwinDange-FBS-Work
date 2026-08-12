# 1 to 9
for i in range(1 , 6):
    k = 1
    for j in range(1 , 6 - i):
        print(" " , end =" ")

    for j in range(1 , i + 1):
        print(k, end =" ")
        k += 1

    for j in range(1 , i):
        print(k, end =" ")
        k += 1

    print()

# A to I
for i in range(1, 6):
    k = 1

    for j in range(1, 6 - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    k += 1

    for j in range(1, i):
        print(chr(64 + j + i), end=" ")
    k += 1

    print()