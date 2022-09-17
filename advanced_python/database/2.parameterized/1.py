#  ============ Parameterized Query =============
#
#  A parameterized query is query which can use the format or pyformat parameterization 
#  style for parameters and the parameter values supplied at execution.
#
#  These executed with MySQLCursor can use the %s and %(key)s format style.
#
#  %s is used as format style in the sql queries, while using tuple parameters.
#
#  %(key)s is used as format style in the sql queries, while using dictionary parameters.
#
#

# =================== Tuple Parameters =================
#
#  myc = conn.cursor()
#  
#  sql = 'INSERT INTO  student (name, roll, fees) VALUES (%s, %s, %s)' 
#
#  params = ("Rohan", 111, 5000.23)
#
#  myc.execute(sql, params)


# =================== Dictionary Parameters ====================
#
#  myc = conn.cursor()
#  
#  sql = 'INSERT INTO  student (name, roll, fees) VALUES (%(name)s, %(roll)s, %(fees)s)' 
#
#  params = {'name': 'Rahul', 'roll': 111, 'fees': 5000.23}
#
#  myc.execute(sql, params)

