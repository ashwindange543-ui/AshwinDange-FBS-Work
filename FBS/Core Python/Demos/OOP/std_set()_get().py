class Student:
    def __init__ (self , rollno , name , marks):
        self.rollNo=rollno
        self.name=name
        self.marks=marks

    def getName(self):
        return self.name
    def setName(self , newName):
        self.name=newName
    
    def getMarks(self):
        return self.marks
    def setMarks(self , newMarks):
        self.marks=newMarks
    
    def getRollNo(self):
        return self.rollNo
    def setRollNo(self , newRollNo):
        self.rollNo=newRollNo

    def display(self):
        print(F"RollNo={self.rollNo},Name={self.name},Marks={self.marks}")

s1 = Student(12 , "Ritish" , 45)
s2 = Student(24 , "Pramod" , 39)
s1.display()
s2.display()
s1.name="Rahul"
s1.display()
s2.marks=89
s2.display()
print(s2.rollNo)
