class Employee:
    def __init__ (self , eid , ename , esal):
        self.id=eid
        self.name=ename
        self.sal=esal
    def display(self):
        print(F"Id={self.id},Name={self.name},Sal={self.sal}")

e1 = Employee(12 , "Ritish" , 90472)
e2 = Employee(24 , "Pramod" , 72492)
e1.display()
e2.display()
print(e1.sal)
print(e2.name)