m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))
m4 = int(input("Enter Marks 4: "))
m5 = int(input("Enter Marks 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

if(per >= 75):
    print("Distinction")
elif(per >= 60):
    print("First Class")
elif(per >= 50):
    print("Second Class")
elif(per >= 35):
    print("Pass")
else:
    print("Fail")