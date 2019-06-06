from datetime import timedelta, datetime
import pandas as pd
# # aim:
#
# a time range from a to b with value x should be split into intervals
# each intervall should hold a fraction of x
#
# example:
# # data:


start = datetime(2019, 1, 1, 21, 30, 0, 0) #2019-01-01 21:00:00
end = datetime(2019, 1, 3, 6, 30, 0, 0) #2019-01-03 06:00:00
val = 66

# # solution:
intervalls = [
    (datetime(2019, 1, 1),  6),
    (datetime(2019, 1, 2), 48),
    (datetime(2019, 1, 3), 12)
]

print(start, end, val)
print(intervalls)

############################################################################

a = min(start, end)
b = max(start, end)
x = val

span = (b - a).total_seconds()
xp = x / span
print(span, xp)


cur_time = a.replace(microsecond=0,second=0,minute=0)
times = []
vals = []
print(cur_time, times, vals)

while cur_time < b.replace(microsecond=0,second=0,minute=0,hour=0)+timedelta(hours=1):
    times.append(cur_time)
    # vals.append()
    cur_time = cur_time + timedelta(hours=1)
    print(cur_time)

print(times, vals)
