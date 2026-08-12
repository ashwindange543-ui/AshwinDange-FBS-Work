feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_inches = feet * 12 + inches
cm = total_inches * 2.54
meter = cm / 100

print("Distance =", meter, "meters")
print("Distance =", cm, "centimeters")