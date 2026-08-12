for i in range(1 , 6):
    print(" " * (14 - i), end="")
    print("*", end="")

    if(i > 1):
        print(" " * (2 * i - 3), end="")
        print("*", end="")

    print()

for i in range(5, 0, -1):
    print(" " * (14 - i), end="")
    print("*", end="")

    if(i > 1):
        print(" " * (2 * i - 3), end="")
        print("*", end="")

    print()


