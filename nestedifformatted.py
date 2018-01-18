a=10
b=20
c=300
print("a={0},b={1},c={2}".format(a,b,c))
if a>b:
    if a>c:
        print("a={0} is big".format(a) )
    else:
        print("c={0} is big".format(c))
else:
    if b>c:
        print("b={0} is big".format(b))
    else:
        print("c={0} is big".format(c))
