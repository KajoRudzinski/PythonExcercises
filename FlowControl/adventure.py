available_exits = [
    "n",
    "s",
    "e",
    "w"
]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Choose direction: ")

print("good")