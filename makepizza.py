def doughtype ():
    doughs = ["Traditional", "Thin", "Cheese Border"]

    print (" Available doughs:")
    for i, dough in enumerate(doughs, start=1):
        print (f"{i}. {dough}")
    select =  int(input("Select the type of dough (1-3): ")) - 1
    return doughs[select]


def saucetype ():
    sauces = ["Tomato", "Alfred", "BBQ", "Pesto"]

    print (" Available Sauces:")
    for i, sauce in enumerate(sauces, start=1):
        print (f"{i}. {sauce}")
    select =  int(input("Select the type of sauce (1-4): ")) - 1
    return sauces[select]


def modifyingt(ingredients):
    #assimilate ingt as ingredients
    ingts = [
        "Tomato", "Mushrooms", "Olive", "Onion",
        "Chicken", "Ham", "Meat", "Bacon", "Cheese"
    ]

    print (" Available Ingredients:")
    for i, ingt in enumerate(ingts, start=1):
        print (f"{i}. {ingt}")

    print ("\n Actual ingredients selected:")
    print (", ".join(ingredients) if ingredients else "None Selected")

    option = input("Do you want to add or remove ingredients? (Add / Remove)\n").lower()

    if option == "add":
        selections = input("Select the ingredients please (e.g., 1 2 Up to 7): ")
        indexes = [int(i) - 1 for i in selections.split() if i.isdigit()]
        for index in indexes:
            if ingts[index] not in ingredients:
                ingredients.append(ingts[index])
    elif option == "remove":
        selections = input("Select the ingredients to remove (e.g., 1 2 Up to 7): ")
        indexes = [int(i) - 1 for i in selections.split() if i.isdigit()]
        for index in indexes:
            if ingts[index] in ingredients:
                ingredients.remove(ingts[index])
    return ingredients


def showpizza(dough, sauce, ingredients):
    print ("\n Pizza Order Preview: \n")
    print (f"Dough:{dough}")
    print (f"Sauce:{sauce}")
    print (f"Ingredients:{", ".join(ingredients) if ingredients else "None Selected"}\n")