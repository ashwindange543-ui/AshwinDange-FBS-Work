
class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def Display(self):
        print("Employee ID:", self.eid)
        print("Employee Name:", self.ename)
        print("Basic Salary:", self.basic)


e1 = Emp(101, "Rahul", 25000)
e1.Display()
