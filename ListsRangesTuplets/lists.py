# 2 ways of creating empty lists
list_1 = []
list_2 = list()

print("list 1: {}".format(list_1))
print("list 2: {}".format(list_2))

if list_1 == list_2:
    print("List are equal")

# Passing members of a string
# because string is iterable
# to new list:

print(list("The new list"))

even = [2, 4, 6, 8]
another_even = even

print(another_even is even)
# returns true > for python these are the same

# BUT...:
another_even_x = list(even)
print(another_even_x is even)
# returns false

# BUT...:
print(another_even_x == even)
# returns true, because it compares the content
# not object identity

odd = [1, 3, 5, 7]

numbers = [even, odd]  # creates list with 2 lists in them
print(numbers)

for number_set in numbers:
    print(number_set)
    for value in number_set:
        print(value)