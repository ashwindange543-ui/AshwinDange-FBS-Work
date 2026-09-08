li = [10 , 20 , 10 , 30 , 40]
num = int(input("Enter the number: "))
count = 0
for i in range(len(li)):
    if li[i] == num:
        count += 1
if count > 0:
    print("Element is present")
    print("Occurrences =", count)
else:
    print("Element is not present")