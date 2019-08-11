from datetime import datetime
from datetime import timedelta
import time, sys

import module.read.pi as rpi
ram = rpi.virtual_memory()

print(datetime.now())
print("> CPU: {}%".format(rpi.cpu_percent()))
print("> RAM: {}%".format(ram.percent))
