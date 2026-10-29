#write a program age of a person
#   raise is used to raise the Exception with our customsiable   (syntax- raise exception (msg))
# this example of inbuilt exception 

from myexception import MyException
try:
    age=int(input('Enter the age= '))
    if age<=0:
        #m=MyException(age)
        raise MyException(age)  # konsa bi vale le sakte like valueError, ZeroDivisionError
except Exception as m:
    print(m)
except Exception as e:
    print(e)