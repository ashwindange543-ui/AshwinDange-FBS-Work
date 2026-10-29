class Student:
    inName="FBS"
    stdCount=0
    def __init__(self,rollno,name,batch):
        self.rollNo=rollno
        self.name=name
        self.batch=batch
        Student.stdCount+=1
    def setRollno(self,nron):
        self.rollNo=nron
    def display(self):
        print(f"RollNo={self.rollNo},Name={self.name},Batch={self.batch}")
class PlaceedStudent(Student):
    def __init__(self,rollno,name,batch,cName):
        super().__init__(rollno,name,batch)
        self.cName=cName
    def display(self):
        print(f"cName={self.cName}")
        return super().displya()

s1=Student(12,"Suraj",1234)
s2=PlaceedStudent(1,"Shankr",1232,"GlobalPayment")
print(Student.stdCount)
