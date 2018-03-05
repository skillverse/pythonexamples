import os 
dir=os.getcwd()
files=os.listdir(dir)
# Files in Current Directory
for i in files:
    n=str(i)
    if(n.find("txt")>0):
        print(str(i))
        

