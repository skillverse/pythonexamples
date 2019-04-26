import mysql.connector
config = {
    'user': 'mtcet',
    'password': 'mtcet',
    'host': '127.0.0.1',
    'port':'3306',
    'database':'mtcet'      
     }
cnx=mysql.connector.connect(**config)
curs=cnx.cursor(buffered=True)
curs.execute("select * from feedback")
records=curs.fetchall()
for data in records:
    print(data[2]," ",data[1])
curs.close()
cnx.close()      
        




