#wap to create class of emp and add the emp object into a file
import pickle
class Employee():
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getid(self):
        return self.id
    def setid(self, newid):
        self.id = newid

    def getname(self):
        return self.name
    def setname(self, newname):
        self.name = newname

    def getsal(self):
        return self.sal
    def setsal(self, newsal):
        self.sal = newsal

    def display(self):
        print(f'id = {self.id}\tName={self.name}\tsal = {self.sal}')

    def __str__(self):    
        return f'{self.id}\t{self.name}\t{self.sal}'

e1=Employee(10, 'Hardik', 124000)
e2=Employee(11, 'Prakash', 578000)
e3=Employee(19, 'Ankit', 121110)

with open('demo.txt', 'w') as fw:
    fw.write(str(e1))
    # fw.write(str(e2))
    # fw.write(str(e3))

with open('demo.txt', 'r') as fr:
    # data=fr.read()
    # print(data)
    # e1=data.split()   # aap jo parameter pass karoge usko split karega in the form of list
    # print(e1)
    # eid=(data[0])
    # name=int(data[1])
    # sal=(data[2])
    # emp=Employee(eid,name,sal)
    # emp.setname('Harman')
    # print(emp)   

    f=open('emp.dat', 'wb')
    # print(f.tell())
    # pickle.dump('Objectname','Object of file')
    pickle.dump(e1,f)       #for storing purpose use dump
    pickle.dump(e2,f)
    pickle.dump(e3,f)
    fr=open('emp.dat','rb')
    # print(f.tell())
    f.seek(0)
    data=pickle.load(fr)    #pikal.load gives 1 parameter -file ka object (for reading purpose use load)
    # print(type(data))
    # print(data.getName)
    data1=pickle.load(fr)
    data2=pickle.load(fr)
    # data3=pickle.load(fr)   #ran out of input- 3 object store kele load 4 ved call kele manun ran out of input det aahe
    print(data)
    print(data1)