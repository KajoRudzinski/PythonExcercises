numbers = [1, 45, 16, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")

# the else in the loop will only executed
# if the loop runs to the end normally
# if it breaks else statement will be skipped
