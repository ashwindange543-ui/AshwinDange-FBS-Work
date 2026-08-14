#1. To make parameter optional
#2. parameter - default (Assigning value to parameter in function definition)
#3. If we pass value to default para, it takes passed value
     #If we don't pass value to default para, it takes default value
#4. Flow from right to left

def emp(id , name='' , sal=0 , dept = 'Backoffice'):
    print('ID:',id)
    print('Name:',name)
    print('SALARY:',sal)
    print('DEPARTMENT:',dept)

emp(101 , 'ABC' , 50000 , 'IT')
print('#####################')
emp(102 , 'XYZ' , 10000 )