answer = 5

print("Please guess the number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please get higher")
    guess = int(input())
    if guess == answer:
        print("Correct!")
    else:
        print("not correct")
elif guess > answer:
    print("Please get lower")
    guess = int(input())
    if guess == answer:
        print("Correct!")
    else:
        print("not correct")
else:
    print("You got it right")
