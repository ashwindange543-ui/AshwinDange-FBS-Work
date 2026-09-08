total = 0

for i in range(1, 6):
    price = float(input("Enter price of product: "))
    total = total + price

gst = total * 18 / 100
bill = total + gst

print("Total amount:", total)
print("GST (18%):", gst)
print("Final Bill:", bill)