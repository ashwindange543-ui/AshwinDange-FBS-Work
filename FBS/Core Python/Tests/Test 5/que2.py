n = int(input("Enter original number of coins: "))

li = list(map(int, input("Enter coins: ").split()))

for i in li:
    if li.count(i) % 2 != 0:
        print("Missing coin =", i)
        break