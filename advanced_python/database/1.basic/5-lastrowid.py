#  ============ lastrowid Property =============
# 
#  This read-only property returns the value generated for an AUTO_INCREMENT column by 
#  the previous INSERT or UPDATE statement or None when there is no such value available.
#
#  If you perform an INSERT into a table that contains an AUTO_INCREMENT column, lastrowid
#  returns the AUTO_INCREMENT value for the new row.
#
#  If you insert multiple rows into a table using a single INSERT statement, the lastrowid
#  property contains the last insert id of the first row.
#
#  syntax:-       cursor_object.lastrowid 
#
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
sql = "INSERT INTO student(name, city) VALUES ('John', 'Singapur')"

try:
    myc.execute(sql)
    conn.commit()
    print(myc.lastrowid)  
    print(myc.rowcount, "Rows Inserted")
except:
    conn.rollback()
    print("Rollback")


myc.close()
conn.close()



