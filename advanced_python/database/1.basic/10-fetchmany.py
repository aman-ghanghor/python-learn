#  =========== fetchmany() Method ============
#
#  This method fetches the next set of rows of a query result and returns a list of tuple.
#  If no more rows are available, it returns an empty list.
#
#  The number of rows returned can be specified using the size argument, which defaults to 
#  one. Fewer rows are returned if fewer rows are available than specified.
#
#  You must fetch all rows for the current query before executing new statements using the 
#  same connection
#
#
#  Syntax:-   rows = cursor_object.fetchmany(size=1)
#
#  ex:-   rows = myc.fetchmany(3)



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


myc = conn.cursor(buffered=True)
sql = "SELECT * FROM student"

try:
    myc.execute(sql)
    rows = myc.fetchmany(3)
    print(rows)
except:
    conn.rollback()
    print("Rollback")



myc.close()
conn.close()


