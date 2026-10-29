class Employee:
    def __init__ (self , eid , ename , esal):
        self.id=eid
        self.name=ename
        self.sal=esal

    def getName(self):
        return self.name
    def setName(self , newName):
        self.name=newName

    def getSal(self):
            return self.sal
    def setSal(self , newSal):
            self.sal=newSal

    def getID(self):
            return self.id
    def setID(self , newID):
            self.id=newID
    
    def display(self):
        print(F"Id={self.id},Name={self.name},Sal={self.sal}")

e1 = Employee(12 , "Ritish" , 90472)
e2 = Employee(24 , "Pramod" , 72492)
e1.display()
e2.display()
#e1.name="Virat"
e1.setName("Virat")
e1.display()
print(e2.getSal())
e2.setSal(12121212)
#print(e2.getName() ," ",  e2.setSal())

print("Employee" ,[e1])