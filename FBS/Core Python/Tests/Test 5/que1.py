D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter amount: "))

count = 0

for note in D:
    n = amount // note
    count = count + n
    amount = amount % note

print("Minimum notes =", count)