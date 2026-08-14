#1. To neglect positional parameter concept
#2. Assign value to parameter in function call
#3. Parameter name in function definition
   # and function call should be same
#4.Flow from right to left


def emp(id , name , sal , dept):
    print('ID:',id)
    print('Name:',name)
    print('SALARY:',sal)
    print('DEPARTMENT:',dept)

emp(name ='ABC' ,sal = 50000 , dept ='IT' , id = 101)
print('#####################')
emp(102 , 'XYZ' , dept ='IT' ,sal = 10000 )