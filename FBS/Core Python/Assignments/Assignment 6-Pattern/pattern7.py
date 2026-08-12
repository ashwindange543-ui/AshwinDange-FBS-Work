# first Way
n = 5

for i in range(1, n + 1):
    for space in range(n - i):
        print("  ", end="")

    for j in range(1, 2 * i):
        print(chr(64 + j), end=" ")

    print()

# Second Way
for i in range(1 , 6):
    for j in range(6 - i):
        print(" " , end =" ")

    for j in range(1 ,2 * i):
        print(chr(64 + j), end =" ")

    print()


# Third way
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