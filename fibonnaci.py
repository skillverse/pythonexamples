clear
import sys
def cube(n): #generator function
        if(n<0):
            return
        yield n*n*n

c = cube(9)
while True:
    try:
        print (next(c), end=" ")
    except StopIteration:
        sys.exit()
