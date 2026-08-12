# Frist way
n = 5

for i in range(1, n + 1):
    print('  ' * (n - i), end='')

    for j in range(1, 2 * i):
        print(j, end=' ')

    print()

# Second Way
for i in range(1 , 6):
    for j in range(6 - i):
        print(" " , end =" ")

    for j in range(1 ,2 * i):
        print(j, end =" ")

    print()

# Third Way
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