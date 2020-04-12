parrot = "Norwegian Blue"

print(parrot)
print(parrot[3])    # print individual char, 0 based: "w"

print()

print(parrot[-1])       # from behind, starting from -1: "e"
print(parrot[13-14])    # the same (-1): "e"

# string slicing

# [starts at including:ends not including]
print(parrot[0:6])      # Norweg
print(parrot[3:5])      # we
print(parrot[0:9])      # Norwegian
print(parrot[:9])       # Norwegian

print(parrot[10:14])    # Blue
print(parrot[10:])      # Blue

print(parrot[:6] + parrot[6:])  # Norwegian Blue

# slicing with step
print(parrot[0:6:2])    # Nre > every 2nd char
print(parrot[0:6:3])    # Nw  > every 3rd char

number = "9,223:902;222 523:333,980"
separators = number[1::4]
print(separators)   # could be useful working with weird data

