splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

# using \ with quotes

print('The pet shop owner said "No, no, \'e\'s uh,... he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,... he's resting\".")

# tripple quotes
print("""The pet shop owner saig "No, no, 'e's uh,... he's resting".""")

anotherSplitString = """This string has been
split over
several
lines"""

print(anotherSplitString)

notSplitString = """This string has not been \
split over \
several \
lines"""

print(notSplitString)

print("C:\\Users\\someone\\notes.txt")  # escape with \
print(r"C:\Users\someone\notes.txt")    # escape with r (used for raw text - regexp)
