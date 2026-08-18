import math
days = 500

years = days // 365   # 1
days = days % 365     # 135
weeks = 135 // 7      # 19
day = 135 % 7         # 2
print("Years is ",years)
print("Days is ",days)
print("Weeks is ",weeks)
print("Days is",day)