# 1. pass : to neglest expected indented block error

for i in range(1 , 10):
    pass

# 2. break : to stop the loop

for i in range(1 , 10):
    if(i == 3):
        break
    print(i)

# 3. continue : to stop current iteration

for i in range(1 , 10):
     if(i == 3):
         continue
     print(i)

# 4. else : will execute when loop executed successful

for i in range(1 , 10):
   # print(i)

    #if(i == 5):
    #  break
    #print(i)

    if(i == 5):
       continue
    print(i)
else:
    print("Else executed")

    
