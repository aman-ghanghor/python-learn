#  ========== rowcount Property ==========
#  
#  This read-only property returns the number of rows returned for SELECT statement, or the
#  number of rows affected by DML, statement such as INSERT or UPDATE.
#
#  Syntax:-     cursor_object.rowcount
#






#  Create Connection
import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='Aman@1234',
        host='localhost',
        port='3306',
        database='mydb'
    )
    print("Connected")
except:
    print('Unable to connect')


myc = conn.cursor()
sql = "INSERT INTO student(name, city) VALUES ('Krishna', 'Agra'), ('Hari', 'Bhopal')"

try:
    myc.execute(sql)
    conn.commit()
    rowsAffected = myc.rowcount ;
    print(rowsAffected, "Rows Inserted")
except:
    conn.rollback()
    print("Rollback")


myc.close()
conn.close()










