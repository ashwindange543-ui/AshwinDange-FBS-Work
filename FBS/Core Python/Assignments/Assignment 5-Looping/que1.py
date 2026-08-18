userid = "admin"
password = "1234"

for i in range(3):
    u = input("Enter User ID: ")
    p = input("Enter Password: ")

    if(u == userid and p == password):
        print("Login Successful")
        break
    else:
        print("Wrong User ID or Password")

else:
    print("Account Locked")