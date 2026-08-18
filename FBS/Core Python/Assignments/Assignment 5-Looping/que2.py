n = int(input("Enter number of students: "))

total_per = 0

for i in range(n):
    print("\nStudent", i + 1)

    total = 0

    for j in range(5):
        mark = int(input("Enter mark: "))
        total = total + mark

    per = total / 5
    print("Percentage =", per)

    total_per = total_per + per

print("\nAverage Percentage =", total_per / n)