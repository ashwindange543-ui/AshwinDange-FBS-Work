area = float(input("Enter area of one  wall:"))
interior_cost = float(input("Enter cost of interior wall:"))
exterior_cost = float(input("Enter cost of exterior wall:"))

interior = area * interior_cost
exterior = area * exterior_cost

total_cost = interior + exterior

print(" Interior painting cost= ", interior)
print(" Exterior painting cost= ", exterior)
print(" Total printing cost+ ", total_cost)