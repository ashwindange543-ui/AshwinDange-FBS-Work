class Student:
    def __init__ (self , rollno , name , batch):
        self.rollNo=rollno
        self.name=name
        self.batch=batch

    def getName(self):
        return self.name
    def setName(self , newName):
        self.name=newName
    
    def getBatch(self):
        return self.batch
    def setBatch(self , newBatch):
        self.batch=newBatch
    
    def getRollNo(self):
        return self.rollNo
    def setRollNo(self , newRollNo):
        self.rollNo=newRollNo

    def display(self):
        print(F"RollNo={self.rollNo},Name={self.name},Batch={self.batch}")

s1 = Student(12 , "Suraj" , "JulyPython")
s2 = Student(13 , "Swaraj" , "JulyPython")
s3= Student(1 , "Ritik" , "JunePython")
s1.display()
s2.display()
s3.display()
#s1.inName="FIrstbitSolution"
Student.inName="FIrstbitSolution"
print("++++++++++++++++++++++++")
s1.display()
s2.display()
s3.display()

