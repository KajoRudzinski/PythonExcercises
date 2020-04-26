import time

print(time.gmtime(0))
# creates a named tuple
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=26, tm_hour=14,
# tm_min=47, tm_sec=52, tm_wday=6, tm_yday=117, tm_isdst=0)

print(time.localtime())

# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=26, tm_hour=16,
# tm_min=47, tm_sec=52, tm_wday=6, tm_yday=117, tm_isdst=1)

print(time.time())  # seconds since start of an epoch 01/01/1970
