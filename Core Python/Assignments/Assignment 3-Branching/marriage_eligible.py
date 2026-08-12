gender = input("Enter Gender (male/female): ")
age = int(input("Enter Age: "))

if(gender == "male" and age >= 21):
    print("Eligible for Marriage")
elif(gender == "female" and age >= 18):
    print("Eligible for Marriage")
else:
    print("Not Eligible")