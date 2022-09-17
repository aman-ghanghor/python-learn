#   ============ commit() Method ============
#
#   This method is used to save inserted row in the table. It is required to make the 
#   changes, otherwise no changes are made to the table.
#
#   This method sends a COMMIT statement to the MySQL server, committing the current
#   transaction. Since by default Connector/Python does not autocommit, it is important 
#   to call this method after every transaction that modifies data for tables that use 
#   transactional storage engines.
#
#   Syntax:-   connection_object.commit()
#
#   Ex:-     conn.commit()
#



#  ============ rollback() Method ==========
#
#  This method is used to un-save row, if there is an error.
#  
#  This method sends a ROLLBACK statement to the MySQL server, undoing all data changes
#  from the current transaction. By default, Connector/Python does not autocommit, so it 
#  is possible to cancel transactions when using transactional storage engines such as InnoDB.
#
#  Syntax:-  connection_object.rollback()


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
sql = "INSERT INTO student(name, city) VALUES ('Rocky', 'London')"

try:
    myc.execute(sql)
    conn.commit()
    print("Inserted Successfully")
except:
    conn.rollback()
    print("Rollback")


myc.close()
conn.close()










