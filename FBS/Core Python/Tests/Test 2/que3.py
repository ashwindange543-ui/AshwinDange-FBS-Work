import math

radius = 20
length = 50
breadth = 40
cost = 35

circle = 2 * math.pi * radius
rectangle = 2 * (length + breadth)

total_fencing = (circle + rectangle) * 5
total_cost = total_fencing * cost

print("Total fencing:", total_fencing)
print("Total cost:", total_cost)