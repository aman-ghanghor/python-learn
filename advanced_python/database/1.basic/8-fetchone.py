#  ============ fetchone() Method =============
#
#  This method retrieves the next row of a query result set and returns a single sequence,
#  or None if no more rows are available. By default, the returned tuple consists of data
#  returned by the MySQL server, converted to Python objects. If the cursor is a raw cursor, 
#  no such conversion occurs.
#
#  You must fetch all rows for the current query before executing new statements using the 
#  same connection
#
#  Syntax:-   row = cursor_object.fetchone()
#
#
#
#
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
sql = "SELECT * FROM student"

try:
    myc.execute(sql)
    row = myc.fetchone() 
    while row is not None:
        print(row)
        row = myc.fetchone()

except:
    conn.rollback()
    print("Rollback")





myc.close()
conn.close()



