import time
from _datetime import datetime
from dateutil import tz


# time_now = str(str(time.time()).replace('.',''))[:-3]

nows = datetime.now().timestamp()
nows = str(str(nows).replace('.',''))[:-3]
print(nows)
today = datetime.utcnow().date()
start = datetime(today.year, today.month, today.day, tzinfo=tz.tzutc()).timestamp()
start = str(str(start).replace('.',''))[:-3]
print(start)
f = int(nows) - int(start)
print(f)