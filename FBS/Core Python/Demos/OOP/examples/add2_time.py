class Time:
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = sec 
    def __str__(self):
        return f"{self.hr} : {self.min} : {self.sec}"
    def __odd__(self , other):
        thr=self.hr+other.hr
        tmin=self.min+other.min
        tsec=self.sec+other.sec
        t=Time(thr , tmin , tsec)
        return 
    
t1 =Time(12 , 4 , 6)
t2 =Time(1 , 5 , 6)
#print(t1)
#print(t2)
print(t1 + t2)
