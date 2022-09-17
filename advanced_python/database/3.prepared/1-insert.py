#  ===============  Prepared Statement  ================
#
#  A prepared statement is used to execute the same statement repeatedly with high efficiency.
#  The prepared statement execution consists of two stages; prepare and execute.
#
#  At the prepare stage a statement template is sent to the database server. The server performs 
#  a syntax check and initializes server internal resources for later use.
#
#  At the execution Stage the parameter vaues are send to the server. The server creates a
#  statement from the statement template and these values to execute it.
#
#  Prepared statements executed with MySQLCursorPrepared can use the format % or qmark ? 
#  parameterization style.
#
#  %s and ? are called as parameter marker.
# 
#  This differs from non-prepared statements executed with MySQLCursor, which can use the format
#  or pyformat parameterization style.
#



#  =============== Advantages ================
#
#  * Prepared statements are very useful against SQL injections.
#
#  * Prepared statements reduce parsing time as the preparation on the query is done only once
#    (although the statement is executed multiple times.)
#



#  =============== Creating a Cursor ================
# 
#  Using [prepared=True] argument to the cursor() method, creates a cursor that enables execution
#  of prepared statements using the binary protocol.
#
#  In this case, the cursor() method of the connection object returns a MySQLCursorPrepared object.
#
#  e.g :-  
#         myc = conn.cursor(prepared=True)


#    sql = 'INSERT INTO student(name, roll, fees) VALUES (%s, %s, %s)' ;
#    myc = conn.cursor(prepared=True)
#    params = ('Rahul', 102, 2300.52)
#    myc.execute(sql, params)


#    sql = 'INSERT INTO student(name, roll, fees) VALUES (%?, %?, %?)' ;
#    myc = conn.cursor(prepared=True)
#    params = ('Rahul', 102, 2300.52)
#    myc.execute(sql, params)




#  =========== How it works ===========
#
#  * For the first call to the execute() method, the cursor prepares the statement.
#    If data is given in the same call, it also executes the statement and you should fetch the data.
#
#  * For subsequent execute() calls that pass the same SQL statement, the cursor skips
#    the preparation phase.


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


sql = 'INSERT INTO student(name, city) VALUES (%s, %s)'
# sql = 'INSERT INTO student(name, city) VALUES (%?, %?)'
myc = conn.cursor(prepared=True)      # MySQLCursorPrepared
params = ('Sachin', 'Mumbai')


try:
    myc.execute(sql, params)
    conn.commit()
    print(myc.rowcount, "Rows inserted")
except:
    conn.rollback()
    print("Unable to Insert")


myc.close()                                                                                                                         
conn.close()