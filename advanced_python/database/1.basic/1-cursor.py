# =========== cursor() Method ============
#
#  This method is used to create cursor class object.
#  We need cursor object so we can call execute() method.
#
#  Syntax :-
#            cursor_object = connection_object.cursor()
#
#  - Argument may be passed to cursor() method to control what type of cursor to create:
#
#  * If [buffered] is True, the cursor fetches all rows from the server after an operation is executed.
#    This is useful when queries return small result sets. buffered can be used alone, or in combination
#    with the dictionary or named_tuple argument.
#
#  * If [dictionary] is True, the cursor returns rows as named tumples.
#
#  * If [named_tuple] is True, the cursor returns rows as named tuples.
#
#  * If [prepared] is True, the cursor is used for executing prepared statements.
#
#  * If [row] is True, the cursor skips the conversion from MySQL data types to Python types when fetching rows.
#    A rows cursor is usually used to get better performance or when you want to do the conversion yourself.
#
#  * The [cursor_class] argument can be used to pass a class to use for instantiating a new cursor. It must be a
#    subclass of cursor.cursorBase.
#
#
#  - The returned object depends on the combination of the arguments. Example:
#
#  * If not buffered and not raw: MySQLCursor
#
#  * If buffered and not raw: MySQLCursorBuffered
#
#  * If not buffered and raw: MySQLCursorRaw
#
#  * If buffered and raw: MySQLCursorBufferedRaw
#
#   eg:-  myc = conn.cursor()  ------> MySQLCursor
#
#   eg:-  myc = conn.cursor(buffered=True)  ------> MySQLCursorBuffered
#
#   eg:-  myc = conn.cursor(prepared=True)  ------> MySQLCursorPrepared



#   ========== execute() Method ==========
#
#   This method is used to execute given SQL queries.
#   We need cursor object so we can call execute() method.
#   Syntax:-
#           cursor_object.execute(sql, param=None, multi=False)
#
#   >>  sql = It is sql query.
#   >>  param = The parameters found in the tuple or dictionary params are params are bound to
#               the variables in the operation.
#   >>  multi = execute() returns an iterator if multi is True.
#
# 
#   Example:-
#            myc = conn.cursor()
#            myc.execute('SELECT * FROM student')
#
#   Example:-
#            sql = 'SELECT * FROM student'
#            myc = conn.cursor()
#            myc.execute(sql)



#  =========== Close Cursor ============
#
#  close() method closes the cursor, rests all results, and ensures that the cursor object has
#          no reference to its original connection object.
#
#  Syntax:-  cursor_object.close()
#            
#  eg:-  myc.close()




# Creating Connection
import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='Aman@1234',
        host='localhost',
        port=3306
    )
    print(conn.is_connected())
    print("Connected to Database")
except:
    print('Unable to Connect')


# create cursor object
myc = conn.cursor()
sql = 'SHOW DATABASES'
myc.execute(sql)

for d in myc:
    print(d)



myc.close()
conn.close()


















