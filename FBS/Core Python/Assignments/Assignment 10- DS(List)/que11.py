li = [10, 15, 20, 30, 40, 60, 75, 90]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

for i in range(len(li)):
    if li[i] % m == 0 and li[i] % n == 0:
        print(li[i])