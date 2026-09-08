li = [2, 4, 6, 8, 10, 12]

target = int(input("Enter target: "))

pairs = set()

for i in range(len(li)):
    for j in range(i + 1, len(li)):

        if li[i] + li[j] == target:
            pairs.add((li[i], li[j]))

print("Pairs =", pairs)