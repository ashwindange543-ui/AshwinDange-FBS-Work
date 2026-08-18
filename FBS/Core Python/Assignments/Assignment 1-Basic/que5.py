# P = 10000
# R = 20
# T = 2 
P =int(input("Enter Principle Amount 1:"))
R =int(input("Enter Rate 2:"))
T =int(input("Enter Time 3:"))

CI = P * (1 + R/100)**T - P

print("Compound Interest is:", CI)

