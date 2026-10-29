# import math
# print(math.pi)
# print(math.sqrt(36))
# print(math.pow(12,2))
# print(math.factorial(5))  # 5*4*3*2*1
# print(math.ceil(4.1))     #return value in 'int' us se aage wali value deta hai
# print(math.floor(4.9))
# print(math.lcm(4,6))     #list common factor
# print(math.gcd(18,6))
# print(10**2)
# print(math.pow(10,3))
# print(math.sin(0))

# import random
# print(int(random.random()*10000))
# print(random.randint(100,999))    #diffrence betwn randint- isme dono value include hote hai
#   #between that range random vale will be generated
# print(random.randrange(1000,10000)) # ranndrange me last nu. wo exclude hote hai

# li=['Virat', 'MSD', 'Rohit', 'Sachin']
# #print(random.choice(li))       # ye kisi ko bhi print karega ek ek karke
# print(li)
# random.shuffle(li)
# print(li)

import time
# print(time.time())
# for  i in range(1,10):
#     time.sleep(1)
#     print(i)

# print(time.ctime())
# t=time.localtime()
# print(t)
# print(t.tm_year)
# print(t.tm_mday)

import datetime
# date,time,datetime,timedelta
print(datetime.date.today())
print(datetime.datetime.now())
now=datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.min)
print(now.second)


