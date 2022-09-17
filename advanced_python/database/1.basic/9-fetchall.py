#   ============ fetchall() Method =============
#
#   This method fetches all (or all remaining) rows of a query result set and returns
#   a list of tuples. If no more rows are available, it returns an empty list.
#
#   You must fetch all rows for the current query before executing new statements using
#   the same connection.
#
#   Syntax:-    rows = cursor_object.fetchall()
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
    rows = myc.fetchall() 
    print(rows)

except:
    conn.rollback()
    print("Rollback")



myc.close()
conn.close()


