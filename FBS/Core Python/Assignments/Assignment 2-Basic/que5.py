cp = float(input("Enter cost price: "))
discount = float(input("Enter discount (%): "))

sp = cp - (cp * discount / 100)

print("Selling Price =", sp)