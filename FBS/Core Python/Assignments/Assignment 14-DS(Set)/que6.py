li = [-10, -20, 5, 8, 2]

max_product = li[0] * li[1]
num1 = li[0]
num2 = li[1]

for i in range(len(li)):
    for j in range(i + 1, len(li)):

        product = li[i] * li[j]

        if product > max_product:
            max_product = product
            num1 = li[i]
            num2 = li[j]

print("Numbers =", num1, num2)
print("Maximum Product =", max_product)