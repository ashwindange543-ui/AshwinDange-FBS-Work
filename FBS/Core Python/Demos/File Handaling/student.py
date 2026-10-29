import pickle
class Student:
    def __init__(self, rollno, name, batch):
        self.rollno=rollno
        self.name=name
        self.batch=batch

    def getRollno(self):
        return self.rollno
    def setRollno(self,nrollNo):
        self.rollno=nrollNo

    def __str__(self):
        return f'{self.rollno} {self.name} {self.batch}'

s1=Student(12, 'Raj', 93)
s2=Student(32, 'Prabhu', 93)
s3=Student(28, 'Bhagwan', 93)

f=open('xyz.txt', 'w')
# print(type(s1))
f.write(str(s1))
f.seek(0)
fr=open('xyz.txt', 'r')
data=fr.read()
print(data)
# print(type(data)) 
f=open('xyz.txt', 'wb')
pickle.dump(s1,f)   # dump- 2 parameter ghete
pickle.dump(s2,f)   
pickle.dump(s3,f)   
f.seek(0)
fr=open('xyz.txt', 'rb')
d1=pickle.load(fr)
d2=pickle.load(fr)
d3=pickle.load(fr)
print(d1)
print(d2)
print(d3)


# # f=open('xyz.txt', 'wb')
# # pickle.dump(s1,f)
# # pickle.dump(s2,f)
# # pickle.dump(s3,f)
# # f.seek(0)
# fr=open('xyz.txt', '+ab')
# fr.seek(0)
# d1=pickle.load(fr)
# d2=pickle.load(fr)
# d3=pickle.load(fr)
# print(d1)
# print(d2)
# print(d3)
# print(type(d1))
# pickle.dump(Student(1,'Rahul', 45), fr)
# print(fr.tell())
# var=fr.tell()
# fr.seek(var)
# d4=pickle.load(fr)                  
# print(d4) 