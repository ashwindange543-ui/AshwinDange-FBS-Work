#wap to perform division two no by accepting two no from user
try:
    num1=int(input('enter the no 1='))
    num2= int(input('enter the no 2='))
    print(num1//num2)
except ZeroDivisionError as a:
    print(f'I am in zeroDiv',a)

except ValueError as v:
    print(f' Value err={v}')
except Exception as e:
    print(e)
else:
    print('I am in else block')
finally:
    print('I am in finally block')








# wap to create the variable whic contain intiger value and list & print both of them
# a=20 
# print(20)

# li=[10,20,30]
# print(li)

# this all are stored in secondary memory in hard disk(file store permenant type of data)
