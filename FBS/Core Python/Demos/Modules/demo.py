import demo
def add():
    print('Demo=',__name__)

    print(f'Addition={12+18}')
def add1():
    print(f'Addition={12+13}')
def main():
    print('Demo=', __name__)
    add()
    add1()
# main()

if __name__=='__main__':
    print('Demo=',__name__)
    add()
    add1()