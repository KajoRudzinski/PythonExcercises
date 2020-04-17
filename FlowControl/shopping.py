shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy" + item)

# or (better) to exlude item from the loop

for item in shopping_list:
    if item == "spam":
        continue    # 'skips' the remaining code

    print("Buy" + item)