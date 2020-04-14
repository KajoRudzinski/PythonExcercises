parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter.casefold() in parrot: # casefold = lowercase
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")

