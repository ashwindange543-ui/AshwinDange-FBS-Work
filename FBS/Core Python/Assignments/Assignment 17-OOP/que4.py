
class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.StudentId}, {self.Name}, {self.Age}, {self.Percentage}"


class EnggStudent(Student):
    def __init__(self, StudentId, Name, Age, Percentage, Branch, InternalMarks):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Branch = Branch
        self.InternalMarks = InternalMarks

    def Display(self):
        super().Display()
        print("Branch:", self.Branch)
        print("Internal Marks:", self.InternalMarks)

    def CalculateRank(self):
        total = self.Percentage + self.InternalMarks

        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 70:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return super().__str__() + f", {self.Branch}, {self.InternalMarks}"


class MedicalStudent(Student):
    def __init__(self, StudentId, Name, Age, Percentage, Specialization, MarksOfInternship):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Specialization = Specialization
        self.MarksOfInternship = MarksOfInternship

    def Display(self):
        super().Display()
        print("Specialization:", self.Specialization)
        print("Internship Marks:", self.MarksOfInternship)

    def CalculateRank(self):
        total = self.Percentage + self.MarksOfInternship

        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 70:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return super().__str__() + f", {self.Specialization}, {self.MarksOfInternship}"


class College:
    def __init__(self, n):
        self.students = []
        self.n = n

    def AddStudent(self, student):
        if len(self.students) < self.n:
            self.students.append(student)
            print("Student Added Successfully")
        else:
            print("College is Full")

    def GetStudent(self, StudentId):
        for student in self.students:
            if student.StudentId == StudentId:
                return student
        return None

    def RemoveStudent(self, StudentId):
        student = self.GetStudent(StudentId)

        if student is not None:
            self.students.remove(student)
            print("Student Removed Successfully")
        else:
            print("Student Not Found")

    def __str__(self):
        result = "College Students:\n"

        for student in self.students:
            result += str(student) + "\n"

        return result


c1 = College(3)

s1 = Student(101, "Rahul", 20, 80)
s2 = EnggStudent(102, "Amit", 21, 80, "Computer", 85)
s3 = MedicalStudent(103, "Priya", 22, 80, "Cardiology", 85)

c1.AddStudent(s1)
c1.AddStudent(s2)
c1.AddStudent(s3)

print("\n", c1)

student = c1.GetStudent(102)

if student is not None:
    print("\nStudent Found:")
    student.Display()
    print("Rank:", student.CalculateRank())

c1.RemoveStudent(101)

print("\nAfter Removing Student:")
print(c1)
