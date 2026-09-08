num = 1

for i in range(1, 11):

    if i % 2 != 0:
        for j in range(1, 11):
            print(num, end="\t")
            num = num + 1

    else:
        temp = num + 9

        for j in range(1, 11):
            print(temp, end="\t")
            temp = temp - 1

        num = num + 10

    print()