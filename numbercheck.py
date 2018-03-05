class Numbercheck:
    ''' Utility to check the Number'''
    n=0
    def __init__(self,a):
        self.n=a

    def iseven(self):
        if(self.n%2 == 0):
            return True
        else:
            return False
    def isodd(self):
        if(self.n%2 != 0):
            return True
        else:
            return False

nc=Numbercheck(2)
print(nc.iseven())
print(nc.isodd())