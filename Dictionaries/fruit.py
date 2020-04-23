fruit = {"orange":  "a sweet citrus fruit",
         "apple":   "good for making ",
         "lemon":   "a sour, yellow fruit",
         "lime":    "a sour, green citrus"}

print(fruit)

veg = {
    "cabbage": "every child's fav",
    "sprouts": "mmmm, lovely",
    "spinach": "can I have some fruit please"
}

# update (or append rather)

veg.update(fruit)
print(veg)
# now fruit has been appended to veg
# like sql union


# or copy dictionary into the new dict
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
