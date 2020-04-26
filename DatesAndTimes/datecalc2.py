import time

print(time.gmtime(0))

# using the named tuple we can get the item either by index
# or by name
time_here = time.localtime()
print(time_here)
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)
# prints
# Year: 2020 2020
# Month: 4 4
# Day: 26 26


