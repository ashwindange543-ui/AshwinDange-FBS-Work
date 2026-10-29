
import pickle

def Add():
    eid = int(input("Enter ID: "))
    ename = input("Enter Name: ")
    basic = float(input("Enter Salary: "))

    with open("emp.dat", "ab") as f:
        pickle.dump([eid, ename, basic], f)

    print("Record Added")


def Display():
    try:
        with open("emp.dat", "rb") as f:
            while True:
                data = pickle.load(f)
                print(data)
    except (EOFError, FileNotFoundError):
        pass


def Search():
    eid = int(input("Enter ID to Search: "))
    found = False

    try:
        with open("emp.dat", "rb") as f:
            while True:
                data = pickle.load(f)
                if data[0] == eid:
                    print(data)
                    found = True
                    break
    except (EOFError, FileNotFoundError):
        pass

    if not found:
        print("Record Not Found")


def Delete():
    eid = int(input("Enter ID to Delete: "))
    records = []
    found = False

    try:
        with open("emp.dat", "rb") as f:
            while True:
                data = pickle.load(f)
                if data[0] == eid:
                    found = True
                else:
                    records.append(data)
    except (EOFError, FileNotFoundError):
        pass

    with open("emp.dat", "wb") as f:
        for data in records:
            pickle.dump(data, f)

    if found:
        print("Record Deleted")
    else:
        print("Record Not Found")


def Edit():
    eid = int(input("Enter ID to Edit: "))
    records = []
    found = False

    try:
        with open("emp.dat", "rb") as f:
            while True:
                data = pickle.load(f)

                if data[0] == eid:
                    data[1] = input("Enter New Name: ")
                    data[2] = float(input("Enter New Salary: "))
                    found = True

                records.append(data)
    except (EOFError, FileNotFoundError):
        pass

    with open("emp.dat", "wb") as f:
        for data in records:
            pickle.dump(data, f)

    if found:
        print("Record Updated")
    else:
        print("Record Not Found")


while True:
    print("\n1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All")
    print("6. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        Add()
    elif ch == "2":
        Search()
    elif ch == "3":
        Delete()
    elif ch == "4":
        Edit()
    elif ch == "5":
        Display()
    elif ch == "6":
        break
    else:
        print("Invalid Choice")
