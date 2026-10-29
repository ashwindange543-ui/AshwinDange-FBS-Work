# f=None    # Globally define kel
# try:
#     f=open("abcd.txt", 'r')
#     data=f.read()
#     if not data:
#         raise Exception('File me kuch nahi hai')
# except FileNotFoundError as fe:
#     print(fe)
# except Exception as e:
#     print(e)
# else:
#     print(data)
# finally:
#     if f is not None:
#         print('File close ho gayi')
#         f.close()
# print('All task are done.....')


# w- mode = agar file availabe nahi hai to ek file banayega, agar hai to purana data earase karega and new data write karega
#r-mode= ye mode file open karta hai to ek error dega or ek exception through karega ki file not found
# writelines takes the input in the form of list with a comma

#diffrence betwn 
#readlin - pura line read karta hai and stop hota hai 
#readlines - jitne bhi lines aap ke paas availabe hai unko ek list ke form me deta hai 

f=open('abcd.txt','w')
f.write('MI WON 5 CUPS \n RCB WON THE 2 CUPS')
f.writelines(['\n I am good in coding','\n I am not good in Python'])

#append mode- me purana data reserva rahta hai(start from at the end cursor)
f=open('abcd.txt', 'a')
with open('abcd.txt', 'a') as f:
    f.write('\n KKR WON THE 3 CUPS') 

#jitne bite ka data hum write kar rahe utne bite ka data wo remove kar raha(ye avoid karne ke leye hum ise last me rakh denge)
with open('abcd.txt','r+') as f:
    f.writelines('Dc won 1 cup')
    data=f.read()
    print(data) 
    print(f.tell())
    f.write('RR won 1 cup')
    print(f.tell())

with open('abcd.txt', 'a+') as f:  
    print(f.tell())    # (aap ka cursor exact kaha par point out kar raha ye batata hai f.tell()...)a+ mode - at the end cursor position present
    f.seek(19)         # it will take 1 parameter exact index of position(cursor ko jis position me le jana hai waha le jata hai seek method)
    data=f.read()
    print(data)

with open('abcd.txt', 'w+') as f:
    print(f.tell)     # curst start form start (data will be earase in w+ mode)