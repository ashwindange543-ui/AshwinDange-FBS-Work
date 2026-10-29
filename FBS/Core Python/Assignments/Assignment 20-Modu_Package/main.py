
from SY.SYMARKS import SYMARKS
from TY.TYMarks import TYMarks


class Student:
    def __init__(self, rollno, name, sy, ty):
        self.rollno = rollno
        self.name = name
        self.sy = sy
        self.ty = ty

    def CalculateGrade(self):
        total = self.sy.ComputerTotal + self.ty.Theory + self.ty.Practical
        percentage = total / 3

        if percentage >= 70:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def Display(self):
        print("Roll Number:", self.rollno)
        print("Student Name:", self.name)
        print("SY Computer Marks:", self.sy.ComputerTotal)
        print("TY Theory Marks:", self.ty.Theory)
        print("TY Practical Marks:", self.ty.Practical)
        print("Grade:", self.CalculateGrade())


sy1 = SYMARKS(80, 75, 70)
ty1 = TYMarks(85, 90)

s1 = Student(101, "Rahul", sy1, ty1)
s1.Display()
