 # when we open the file in 'r' mode then cursor is present always in starting position
# finally block use : for close the file 
# else block use :  try: block properly execute ho raha to data properly aa raha then use else block

try:
    f = open('abc.txt', 'r')
    data = f.read()

except Exception as e:
    print(e)

else:
    print(data)

finally:
    f.close()

print('I am in outside ABC')
