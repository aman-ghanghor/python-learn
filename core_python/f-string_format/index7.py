# -------------- Format Date and Time ----------------

from datetime import datetime

today = datetime(2022, 3, 13)

print( f"{today:%d-%b-%Y}" )

print( f"{today:%d/%b/%Y}" )

print( f"{today:%d %b, %Y}" )











