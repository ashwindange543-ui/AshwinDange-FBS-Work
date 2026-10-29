class Employee:
    def __init__(self,id,name,sal):
        self.__id=id
        self.__name=name
        self.__sal=sal
        
    def getId(self):
        return self.__id
    def setId(self,neid):
        self.__id=neid
        
        
    def getName(self):
        return self.__name
    def setName(self,newName):
        self.__name=newName
        
        
    def getSal(self):
        return self.__sal
    def setSal(self,nesal):
        self.__sal=nesal
        
    def __str__(self):
        return f"Id= {self.__id} \tName= {self.__name}\tSal={self.__sal}"