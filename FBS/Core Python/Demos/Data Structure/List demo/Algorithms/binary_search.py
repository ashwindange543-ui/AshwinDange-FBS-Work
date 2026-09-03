def binarySearch(li , searchEle):
    beg = 0
    end = len(li) - 1
    while(beg <= end):
        mid = (beg + end) // 2
        if(searchEle == li[mid]):
            return mid
        elif(searchEle < li[mid]):
            end = mid - 1
        elif(searchEle >li[mid]):
            beg = mid + 1
    else:
        return -1


ele = int(input("Enter element to find:"))
li = [10 , 20 , 30 , 40 , 50 , 60]
res = binarySearch(li , ele)
#print(res)
if(res != -1):
    print(f'{ele} is present at index {res}.')
else:
    print(f'{ele} is not present in the list.')