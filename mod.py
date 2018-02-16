import mysql.connector
config = {
    'user': 'vms',
    'password': 'giridher',
    'host': '192.168.31.20',
    'port':'19000',
    'database':'vms'      
     }
cnx=mysql.connector.connect(**config)
curs=cnx.cursor(buffered=True)
curs.execute("select * from users")
records=curs.fetchall()
for data in records:
    print(data)
curs.close()
cnx.close()      
        




