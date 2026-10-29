class A:
    def add(self):
        print("Add A")

class B:
    def add(self):
        print("add B")

class C(B,A):
    def add(self):
        print("Add C")

C1 = C()
C1.add()