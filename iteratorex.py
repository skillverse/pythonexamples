import sys
list1=[1,2,3,4,5,6,7,8,9]
it=iter(list1)
count =0
while 1:
    print(next(it),end=" ")
    count+=1
    if(count%2==0):
        break
while 2:
    try:
        print(next(it))
    except Exception as e:
        sys.exit()
