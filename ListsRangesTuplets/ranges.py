my_list = list(range(10))
print(my_list)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even = list(range(0, 10, 2))
print(even)
# [0, 2, 4, 6, 8]

big_odd = range(1, 10000, 2)
print(big_odd[985])
# 1971 - value at given index of the range

sevens = range(7, 100000, 7)
test = 1449

if test in sevens:
    print("{} is divisible by seven".format(test))

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print(range(0, 5, 2) == range(0, 6, 2))
# True