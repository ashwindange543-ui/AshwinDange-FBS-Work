#1. Direct import
import mypack.xyz
import mypack.abc
mypack.abc.greet()
a=mypack.xyz.iname
print(a)
mypack.xyz.greet1()

#2. From pakagename. modulename import member
from mypack.abc import greet
greet()

#3. From packagename.modulename import members
from mypack.abc import greet
from mypack.xyz import greet1,iname
greet()
print(iname)
greet1()

#4. From packagename.modulename import all(*) members
from mypack.abc import greet
from mypack.xyz import *
greet()
print(iname)
greet1()

#5. Alice Name (nickname)
import mypack.xyz as a
import mypack.abc as b
print(a.iname)
a.greet1()
b.greet() 
