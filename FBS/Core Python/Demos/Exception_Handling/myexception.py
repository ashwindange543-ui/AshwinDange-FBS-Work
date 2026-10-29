class MyException(Exception):
    def __init__(self, *args):
        # print('I am in Constructor of MyException class')
        self.age=args
        print('I am in constructor of MyException class')
    def __str__(self):      # object ko readable format me likha hai to str menthod use hoti hai
        return f'Bhai age proper enter kar de'   #age args ke pass hai (argument tuple format me leta hai, readable format me banana hai to for loop use karo   )