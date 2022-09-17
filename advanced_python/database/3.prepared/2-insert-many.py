#  =========== executemany() Method ============
#
#  This method is used to prepare given SQL query and execute it against all parameter 
#  sequences or mappings found in the sequence seq_of_params.
#
#  With the executemany() method, it is not possible to specify multiple statements to 
#  execute in the sql argument.
#
#  Syntax:-      cursor_object.executemany(sql, seq_of_params)
#  
#  sql = It is sql query
#
#  seq_of_params = It is a list of tuples, containing the data to insert.


import mysql.connector

try:
    conn = mysql.connector.connect(
        user='root',
        password='Aman@1234',
        host='localhost',
        port=3306,
        database='mydb'
    )
    print("Connected Successfully")
except:
    print("Unable to Connect")


# sql = 'INSERT INTO student(name, city) VALUES (%s, %s)'
sql = 'INSERT INTO student(name, city) VALUES (?, ?)'
myc = conn.cursor(prepared=True)      # MySQLCursorPrepared
seq_of_params = [('Sachin', 'Mumbai'), ('Chamu', 'Leh'), ('Ajeet', 'Patna')]


try:
    myc.executemany(sql, seq_of_params)
    conn.commit()
    print(myc.rowcount, "Rows inserted")
except:
    conn.rollback()
    print("Unable to Insert")


myc.close()                                                                                                                         
conn.close()