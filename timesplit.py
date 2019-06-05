from datetime import timedelta, datetime
import pandas as pd
# # aim:
#
# a time range from a to b with value x should be split into intervals
# each intervall should hold a fraction of x
#
# example:
# # data:


a = datetime(2019, 1, 1, 21, 0, 0, 1) #2019-01-01 21:00:00
b = datetime(2019, 1, 3, 6, 0, 0, 2) #2019-01-03 06:00:00
x = 66

# # solution:
intervalls = [
    (datetime(2019, 1, 1),  6),
    (datetime(2019, 1, 2), 48),
    (datetime(2019, 1, 3), 12)
]

print(a, b, x)
print(intervalls)

############################################################################

print((b-a).total_seconds() / x)
