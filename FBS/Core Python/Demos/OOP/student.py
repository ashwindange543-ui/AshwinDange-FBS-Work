class Student:
    def __init__ (self , rollno , name , marks):
        self.rollNo=rollno
        self.name=name
        self.marks=marks
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
