gender = input("Enter gender (M/F):")
age = int(input("Enter age:"))
if(gender == 'F'):
    if(age >= 18):
        print("Girls is eligible for marriage.")
    else:
        print("Pehle padhai kar le")
else:
    if(age >= 21):
        print("Boy is eligible for marriage.")
    else:
        print("Pehle kama lo.")


        
