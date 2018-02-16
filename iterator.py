import sys
list1=[1,2,3,4,5,6,7,8,9]
it=iter(list1)
while 1:
    try:
        print (next(it))
    except Exception as e:
        print ("End  of List")
        sys.exit()
