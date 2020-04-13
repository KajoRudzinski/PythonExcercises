# below, line 4 is not part of the block
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
print("*" * 80)

# below, line 9 is part of the block
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)

# Basically, indentation tells python if this is still that block

# If statements
name = input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))
print(age)

# if age >= 18:
#     print("You're old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {} years".format(18 - age))

# Else if
if age < 18:
    print("Please come back in {} years".format(18 - age))
elif age == 900:
    print("Go away, Yoda!")
else:
    print("You're old enough to vote")
    print("Please put an X in the box")
