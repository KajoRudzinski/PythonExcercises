import shelve

fruit = shelve.open("ShelfTest")
fruit["orange"] = "a sweet, orange citrus"
fruit["apple"] = "good for cider"
fruit["lime"] = "a sour, green citrus"

print(fruit["orange"])
print(fruit["lime"])

fruit.close()
