# below, line 4 is not part of the block
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
print("*" * 80)

# below, line 9 is part of the block
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)

# Basically, indentation tells python if this is still that block

