dinnerChoices = [["Salad", "Soup", "Cheese Plate"],
                 ["Chicken", "Salmon", "Lasagna"]]

appIndex = 0
mainDishIndex = 1
print(dinnerChoices)
print(dinnerChoices[appIndex][mainDishIndex])
print(dinnerChoices[0][0])
dinnerChoices[0][0] = "Steak"
print(dinnerChoices[0][0])

for i in dinnerChoices:
    for j in i:
        print(j, end=" ")
    print()
