import mysql.connector
config = {
    'user': 'vms',
    'password': 'giridher',
    'host': '127.0.0.1',
    'port':'19000',
    'database':'vms'      
     }
cnx=mysql.connector.connect(**config)
curs=cnx.cursor(buffered=True)
curs.execute("select * from users")
records=curs.fetchall()
for data in records:
    print(data[2]," ",data[1])
curs.close()
cnx.close()      
        




