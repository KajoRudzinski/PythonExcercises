string = "123456789"

for char in string:
    print(char)

# normally iterator is created automatically
# for each iterable object
#  but you can create iterator on your own
my_iterator = iter(string)

print(my_iterator)
# this will only give you memory representation like
# <str_iterator object at 0x000001279F1BD3C8>

# better can be tested like
print(next(my_iterator))    # 1
print(next(my_iterator))    # 2... etc