n = int(input("Enter number of passengers: "))
ticket = float(input("Enter ticket price: "))

total = 0

for i in range(n):
    age = int(input("Enter age: "))

    if(age < 12):
        amount = ticket * 0.70
    elif(age > 59):
        amount = ticket * 0.50
    else:
        amount = ticket

    total = total + amount

print("Total Amount =", total)