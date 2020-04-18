import random

highest = 10
lowest = 1
answer = random.randint(lowest, highest)

print("Please guess the number between {0} and {1}: ".format(lowest, highest))
guess = int(input())    # TODO: Finish guessing game

while guess != answer:
    if guess < answer:
        print("Try higher: ")
    else:
        print("Try lower: ")
    guess = int(input())

print("Correct!")


