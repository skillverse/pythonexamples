import requests
url="https://static.pexels.com/photos/36764/marguerite-daisy-beautiful-beauty.jpg"
r= requests.get(url)
print(dir(r))
fo=open("file.jpg","wb")
fo.write(r.content)
fo.close()