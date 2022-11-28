# Python Current Time in a City and State, or Country - https://bit.ly/3u7jnvG
# Time zones - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

#!/usr/bin/env python
from datetime import datetime
import pytz  # $ pip install pytz

print('Asia/Tokyo', datetime.now(pytz.timezone('Asia/Tokyo')))  # you could pass `timezone` object here
print('Europe/Amsterdam', datetime.now(pytz.timezone('Europe/Amsterdam')))  # you could pass `timezone` object here
print('Europe/London', datetime.now(pytz.timezone('Europe/London')))  # you could pass `timezone` object here

# now with TimeZone
print('CZ format:', datetime.now(pytz.timezone('Europe/Amsterdam')).strftime("%d.%m.%Y %H:%M:%S"))
