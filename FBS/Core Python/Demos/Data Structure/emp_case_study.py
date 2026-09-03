emp_details = {}


def addEmp():
    id = int(input("Enter ID: "))
    nm = input("Enter NAME: ")
    dept = input("Enter DEPARTMENT: ")
    sal = float(input("Enter SALARY: "))
    
    if(id not in emp_details):
        emp_details[id] = [id, nm, dept, sal]
        return "Employee added successfully."
    else:
        return "Employee ID already available."

def updEmp():
    id = int(input("Enter ID: "))
    er = emp_details.get(id)
    
    if(er):
        nm = input(f"Enter new NAME({er[1]}): ") or er[1]
        dept = input(f"Enter new DEPT({er[2]}): ") or er[2]
        sal = float(input(f"Enter new SALARY({er[3]}): ") or er[3])
        
        emp_details[id] = [id, nm, dept, sal]
        return "Employee updated successfully."
    else:
        return "ID not found."

def delEmp():
    id = int(input("Enter ID: "))
    
    if(id in emp_details):
        del emp_details[id]
        return "Employee deleted successfully."
    else:
        return "ID not found."

def searchEmp():
    id = int(input("Enter ID: "))
    er = emp_details.get(id)
    
    if(er):
        print("ID:", er[0])
        print("NAME:", er[1])
        print("DEPARTMENT:", er[2])
        print("SALARY:", er[3])
    else:
        print("ID not found.")

def showAllEmp():
    if(emp_details):
        for id, er in emp_details.items():
            print(er)
    else:
        print("No employee found.")

def empManage():
    ch = '0'
    
    while(ch != '6'):
        print("####EMPLOYEE MANAGEMENT####")
        print("""Please select option from below:
1. Add emp
2. Upd emp
3. Del emp
4. Search emp
5. Show all emp
6. Logout""")
        
        ch = input("Enter choice: ")
        
        if(ch == '1'):
            res = addEmp()
            print(res)
            
        elif(ch == '2'):
            res = updEmp()
            print(res)
            
        elif(ch == '3'):
            res = delEmp()
            print(res)
            
        elif(ch == '4'):
            searchEmp()
            
        elif(ch == '5'):
            showAllEmp()
            
        elif(ch == '6'):
            print("Logged out...")
            
        else:
            print("Invalid choice...")

def login():
    print("####LOGIN PAGE####")
    
    uid = "admin"
    passw = "1234"
    
    username = input("Enter USERNAME: ")
    password = input("Enter PASSWORD: ")
    
    if(uid == username and passw == password):
        empManage()
    else:
        print("Invalid credentials...")

def main():
    ch = 0
    while(ch !='2'):
        print('''Please select the option from below :
        1. Login
        2. Exit''')
        ch = input('Enter your choice : ')
        if(ch == '1'):
            login
        elif(ch == '2'):
            print('Thank you for choosing us!')
        else:
            print('Invalid choice...')
main()
