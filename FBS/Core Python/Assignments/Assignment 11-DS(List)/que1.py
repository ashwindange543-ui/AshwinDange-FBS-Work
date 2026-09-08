li = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for i in range(len(li)):
    if li[i] % 2 == 0:
        even += [li[i]]
    else:
        odd += [li[i]]

print("Even List =", even)
print("Odd List =", odd)