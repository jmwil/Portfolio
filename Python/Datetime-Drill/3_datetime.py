import datetime
from pytz import timezone
import pytz

fmt = "%H:%M:%S"

now = datetime.datetime.now(timezone('UTC'))
print('Current time is: ' + now.strftime(fmt))
      
# Portland time
p_now = now.astimezone(timezone('US/Pacific'))
pNow = p_now.strftime(fmt)

# New York time
ny_now = now.astimezone(timezone('US/Eastern'))
nyNow = ny_now.strftime(fmt)

# London time
l_now = now.astimezone(timezone('Europe/London'))
lNow = l_now.strftime(fmt)


p = pNow
if p > "08:59:59":
    if p < "18:00:00":
        print('Portland office is Open')
    else:
        print('Portland office is Closed')

ny = nyNow
if ny > "08:59:59":
    if ny < "18:00:00":
        print('New York office is Open')
    else:
        print('New York office is Closed')

l = lNow
if l > "08:59:59":
    if l < "18:00:00":
        print('London office is Open')
    else:
        print('London office is Closed')
