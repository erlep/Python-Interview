# Python Datetime - https://www.w3schools.com/python/python_datetime.asp

import datetime
import time

# .now()
# import datetime
datetime.datetime.now()
print(datetime.datetime.now())

# .isoformat()
# import datetime
print(datetime.datetime.now().isoformat())

# import time - strftime - https://bit.ly/3Edt2np
print(time.strftime("%Y/%m/%d %H:%M:%S"))

#  sheet_name 25.11.'21 - https://bit.ly/3DDYMkS
print(time.strftime("%d.%m.'%y"))
# print(time.strftime("%-d.%m.'%y")) # '-' no leading zero UNIS
print(time.strftime("%#d.%m.'%y"))  # '#' no leading zero WIN
