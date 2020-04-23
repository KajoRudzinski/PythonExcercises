# sets are immutable
# and unordered

# 1st way to produce set
farm_animals = {
    "sheep",
    "cow",
    "hen"
}
print(farm_animals)

for animal in farm_animals:
    print(animal)
print("*" * 40)

# 2nd way to produce set
wild_animals = set([
    "lion,"
    "tiger",
    "panther",
    "elephant",
    "hare"
])

print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

# to create empty set use onlty:
empty_set = set()

# this creates empty dictionary
empty_dict = {}

# create set with numbers
even = set(range(0, 40, 2))

print(len(even))    # 20 elements

small_even = set(range(0, 40, 2))

# supersets and subsets
print(small_even.issubset(even))    # True
print(even.issuperset(small_even))  # True
