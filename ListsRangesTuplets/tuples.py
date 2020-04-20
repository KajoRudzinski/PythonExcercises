# tuples are basically immutable lists
# you can't append anything to them or update them

# tuples can prevent from unnecessary change
# also good for hashes, dictionary

# exception is changing the list that is stored inside a tuple

t = "a", "b", "c"
print(t)
# returned as ('a', 'b', 'c')

# the same will come out of
print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])

# reminder:
a, b = 12, 13
print(b, a)     # 13, 12

# unpacking the tuple:
title, artist, year = metallica
print(title)    # Ride the Lightning
print(artist)   # Metallica
print(year)     # 1984

# this wouldn't work easily with list
# because at some point someone will update the list

imelda = "More Mayhem", "Imilda May", 2011, \
         (
             (1, "Pulling the Rug"),
             (2, "Psycho"),
             (3, "Mayhem"),
             (4, "Kentish Waltz")
          )

print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
# last line returns
# ((1, 'Pulling the Rug'), (2, 'Psycho'), ...
