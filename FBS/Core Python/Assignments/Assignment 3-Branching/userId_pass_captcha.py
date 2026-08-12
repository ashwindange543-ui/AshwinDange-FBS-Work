import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if(userid == "admin" and password == "1234"):
    num = random.randint(1000, 9999)
    print("Captcha:", num)

    user = int(input("Enter the captcha: "))

    if(user == num):
        print("Login Successful")
    else:
        print("Wrong Captcha")
else:
    print("Invalid User ID or Password")