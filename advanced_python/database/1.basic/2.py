#  ============  Connecting to Database ============
#
#  connect() =  This method is used to open or establish a new connection. It returns an 
#               object representing the connection.
#
#  Syntax:-
#
#          connection_object = connect(user='username', password='pass', database='dbname', host='localhost', port=3306)
#


import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='Aman@1234',
        host='localhost',
        database='mydb',
        port='3306'
    )
    print("Connected...")
except:
    print("Unable to Connect")
    

myc = conn.cursor() ;

sql = "SELECT * FROM student"
myc.execute(sql)

for r in myc:
    print(r)


myc.close()
conn.close()





