# writing to file
cities = [
    "Adelaide",
    "Alice Springs",
    "Darwin",
    "Melbourne",
    "Sydney"
]

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)  # watch out for the 2nd file

cities = []

with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))
# strip removes characters from beginning or end of a string
# here we removed \n denoting end of the line

print(cities)
for city in cities:
    print(city)