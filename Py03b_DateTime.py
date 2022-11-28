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

# days left in year: '
# import datetime; print((datetime.date(2022, 12, 31)-datetime.date.today()).days)
# alias daysleft='python - c "import datetime;print((datetime.date(2022, 12, 31)-datetime.date.today()).days)"'
# print('Days left in year: ', (datetime.date(2022, 12, 31)-datetime.date.today()).days)
print('Days left in year: ', (datetime.date(int(time.strftime("%Y")), 12, 31)-datetime.date.today()).days)

# now with time & datetime.datetime
print('CZ format:', time.strftime("%d.%m.%Y %H:%M:%S"))
print('CZ format:', datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
