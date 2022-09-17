# =============  Database  ==============
#
#  - Database is integrated collection of related information along with the details so that it is
#    available to the several user for the different application

# ============  Requirements ===========
#
#  - SQL = To write sql queries.
#
#  - MySQL = We have to install MySQL in our system. It is an open source database management system
#            application which will help us to manage the database like store and retrieve data.
#
#  - Connector or Driver = A connector is a program that established connection between Python program
#                          and MySQL database without installing connector it if not possible make
#                          communication between python program and MySQL database.


# ============ MYSQL ==============
#
#  It is an open source database management system application which will help us to manage the database
#  like store and retrive data.
#  To work with MYSQL in Python program we have to import [connector] sub module of [mysql] module
#
#  import mysql.connector


# --------- Creating Connection ---------
#
#  connect() = This method is used to open or establish a new connection. It returns an object
#              representing the connection.
#
#  Syntax:-
#          connection_object = connect(user="username", password="pass", host="localhost", port=3306)
#
#  Ex:-
#      conn = mysql.connector.connect(user="root", password="geek", host="localhost", port=3306)
#



# --------- Check Connection ---------
#
#  is_connected() = This method is used to check if the connection to MYSQL is established or not. 
#                   It returns True if the connection is established successfully.



# --------- Close Connection ---------
#
#  close() = This method is used to close the connection.
#  
#  Syntax:-  connection_object.close()






# Creating connection
import mysql.connector

# try:
#     conn = mysql.connector.connect(
#         user='root',
#         password='Aman@1234',
#         host='localhost',
#         port=3306
#     )
#     print(conn.is_connected())
# except:
#     print("Unable to Connect")


config = {
    'user': 'root',
    'password': 'Aman@1234',
    'host': 'localhost',
    'port': 3306
}
try:
    conn = mysql.connector.connect(**config)
    if(conn.is_connected()):
        print("Connected")
        conn.close()
        print(conn.is_connected())
except:
    print("Unable to Connect")
