n = 4

for i in range(n):
    print(" " * (n - i), end="")
    a = 1

    for j in range(i + 1):
        print(a, end=" ")
        a = a * (i - j) // (j + 1)

    print()