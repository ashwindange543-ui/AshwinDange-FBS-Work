unit = int(input("Enter Units: "))

if(unit <= 50):
    bill = unit * 0.50
elif(unit <= 150):
    bill = 50 * 0.50 + (unit - 50) * 0.75
elif(unit <= 250):
    bill = 50 * 0.50 + 100 * 0.75 + (unit - 150) * 1.20
else:
    bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (unit - 250) * 1.50

bill = bill + (bill * 20 / 100)

print("Electricity Bill =", bill)