fo = open("foo.txt", "r+") 
sf=open("ex.py","r")
while(content=sf.read(100)):
    print(content)
fo.close()