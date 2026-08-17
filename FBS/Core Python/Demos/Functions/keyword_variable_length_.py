#1. To pass multiple values with meaning to function
#2. Mention 2 asterisk symbols before parameter name in function definition
#3. Passed data stored in dictionary format
#4. use for loop on dict.items() to get values keys

def emp(**data):
    for key , val in data.items():
        print(key , ' : ' , val)

emp(id  = 101 , age = 35 , add = 'Pune' , sal =50000 , dept = 'Admin')





