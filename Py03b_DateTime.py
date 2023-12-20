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

# Python f-string tips & cheat sheets - https://www.pythonmorsels.com/string-formatting
# datetime podruhe https://cheatography.com/brianallan/cheat-sheets/python-f-strings-basics
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
today = datetime.datetime.today()
print(f"Dnes je: {today}")
print(f"Dnes je: {today:%B %d, %Y}")
print(f"Nazev souboru: soubor_{today:%Y%m%d_%H%M%S}.txt")

# Mereni casu
# record the starting time
start = time.perf_counter()
# some loop
soucet = 0
rozsah = 1_000_001
for i in range(rozsah):
  soucet += i
print(f'for: soucet {rozsah} cisel je {soucet}')
# record the ending time
end = time.perf_counter()
print(f"Time taken: {end - start:.2f} seconds.")

start = time.perf_counter()
soucet = sum(range(rozsah))
print(f'sum: soucet {rozsah} cisel je {soucet}')
end = time.perf_counter()
print(f"Time taken: {end - start:.2f} seconds.")
print("OkDone.")
