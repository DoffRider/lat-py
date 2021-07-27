# import datetime as t
# from datetime import time, timedelta


# sekarang = t.datetime.now().replace(microsecond=0)

# print(sekarang)
# print(sekarang.day)
# print(sekarang.hour)
# print(sekarang.minute)
# print(sekarang.year)
# print("")

# x1 = t.datetime(2021,7,30)

# print(x1)
# print(x1.strftime("%d-%m-%Y"))
# print("")

# hit = x1 - sekarang
# jam = int(hit.seconds/3600)
# menit = hit.seconds/60

# future_time = sekarang + timedelta(seconds=menit)

# print(hit)
# print("")

# print(f"{hit.days} hari {int(hit.seconds/3600)} jam {hit.seconds/60} menit")
# print(future_time)

# print()



# import datetime
  
# # datetime(year, month, day, hour, minute, second)
# a = datetime.datetime(2021, 5, 30, 00, 00, 00)
# b = datetime.datetime(2021, 5, 29, 23, 00, 00)
  
# # returns a timedelta object
# c = a-b 
# print('Difference: ', c)
  
# # returns (minutes, seconds)
# minutes = divmod(c.total_seconds(), 60) 
# print('Total difference in minutes: ', minutes[0], 'minutes',
#                                  minutes[1], 'seconds')
  
# # returns the difference of the time of the day (minutes, seconds)
# minutes = divmod(c.seconds, 60) 
# print('Total difference in minutes: ', minutes[0], 'minutes',
#                                  minutes[1], 'seconds')

import datetime
import time
from datetime import timedelta

# datetime1 = datetime.datetime.now()
datetime1 = datetime.datetime(2021,7,30).replace(microsecond=0)
datetime2 = datetime.datetime.now().replace(microsecond=0)

difference = datetime1 - datetime2
h = float(difference.seconds/3600)
print(f"The time difference between the is: {difference} ||| {str(timedelta(hours=h))}")