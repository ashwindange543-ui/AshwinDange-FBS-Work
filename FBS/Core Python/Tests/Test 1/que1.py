import math

l = float(input("Enger length :"))
b = float(input("Enger breadth :"))
r = float(input("Enger redius :"))

# Area
area = (l * b)+(math.pi * r * r)

# Parimeter 
perimeter = (2 * l) + b + (math.pi * r)

print("Area =", area)
print("Perimeter =", perimeter)
