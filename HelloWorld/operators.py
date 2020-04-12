a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0 (float)
print(a // b)  # 4 integer division, rounded down towards minus infinity
print(a % b)  # 0 modulo: the reminder after integer division

print()

# example on int / float importance:
for i in range(1, 4):
    print(i)

# Following would result in error:
# TypeError: 'float' object cannot be interpreted as an integer
# for i in range(1, a/b):
#    print(i)

# But this will work
for i in range(1, a // b):
    print(i)
