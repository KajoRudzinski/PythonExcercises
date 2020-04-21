# dictionaries aren't accessed by index
# dictionaries are accessed by a key

# example of a dictionary
fruit = {"orange":  "a sweet citrus fruit",
         "apple":   "good for making ",
         "lemon":   "a sour, yellow fruit",
         "lime":    "a sour, green citrus"}
# so it's {key: dictionary}

print(fruit)
print(fruit["lemon"])

# adding
fruit["pear"] = "an odd shaped apple"
print(fruit)    # will include pear

# keys in dictionary are unique
# you will replace the item by adding one
# with the same key

# to delete:
del fruit["lemon"]
print(fruit)

fruit.clear()   # truncates the dictionary
del fruit       # drops the dictionary

fruit = {"orange":  "a sweet citrus fruit",
         "apple":   "good for making ",
         "lemon":   "a sour, yellow fruit",
         "lime":    "a sour, green citrus"}

# looking up wrong key will return an error
print([fruit])


# what you could do is:
# while True:
#     dict_key = input("Enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)   # dictionary.get(dictionary key)
#         print(description)
#     else:
#         print("We don't have that.")

# by default dictionaries are not ordered

# you can order them by using standard list & .sort method or sorted (function)
ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f + "\t - " + fruit[f])

print("#" * 40)

# simpler
for x in sorted(fruit.keys()):
    print(x + "\t - " + fruit[f])

# values of dictionary is also possible but less efficient

print(fruit.items())    # this we can convert into tuple
f_tuple = tuple(fruit.items())
print(f_tuple)

print(dict(f_tuple))    # and convert from tuple back to dictionary

