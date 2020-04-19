# computer to guess the number between 1 and thousand
# according to binary search rules
# (choping result set in half each time with "higher"/"lower" hint)
# this should be done within 10 guesses (because 2^10 = 1024)

low = 1
high = 1000

print("Please think of a number between {} and {}.".format(low, high))
input("press ENTER to start")

guesses = 1
while low != high:
    # print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2  # calculates the midpoint to produce the next guess
    high_low = input("My guess is {}. Should I guess higher or lower? Enter h for higher or l for lower. "
                     "If my guess was correct enter c. "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c as advised.")
    guesses += 1    # the same but more efficient than guesses = guesses + 1
else:
    print("You thought of a number {}".format(low))
    print("I got it in {} guesses!".format(guesses))


# btw python doesn't have a case or switch statement

