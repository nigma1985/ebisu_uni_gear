# Pseudocode:
# 1. random selection:
#   update/not update coordinates table
#
#     1a. if update: run update
#     1b. if error: update all VIEWs
#
# 2. get user data
#   2a. decide on call interval
#
# 3. random selection:
#   call/don't call
#
#   3a. random select:
#     3aa. call list (4/360) --> coordinates >> list of IDs
#     3ab. call prices (350/360) --> list of IDs >> prices
#       --> if error: call list
#     3ac. call detail (6/360) --> one ID >> details
#       --> if error: call list
#
#   3b. ETL results from call
#
#   3c. write data to database

from random import sample, randint, random
import module.read.pi as rpi

ram = rpi.virtual_memory()

if (rpi.cpu_percent() > (2/3*100)) or (ram.percent > (2/3*100)):
    print(datetime.now())
    print("> CPU: {}%".format(rpi.cpu_percent()))
    print("> RAM: {}%".format(ram.percent))
elif random() < 1/6:
    import coordinates_all
else:
    pass
