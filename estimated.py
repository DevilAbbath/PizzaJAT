from makepizza import showpizza

def esttime(ingredients):
    tbase = 20
    ttotal = tbase + len(ingredients) * 2

    print (f"Estimated devilery time is around {ttotal} minutes.")

    return ttotal

def confirm(dough, sauce, ingredients, ttotal):
    print ("Your Order Details: ")
    showpizza(dough, sauce, ingredients)
    print (f" The estimated devilery time is: {ttotal} minutes.\n")
    confirm = input("Do you want to confirm your order? (Yes / No) \n").lower()

    if confirm == "yes":
        print ("\n Order in process, thanks for buy in Pizza JAT")
        return True
    if confirm == "no":
        print ("\n Order cancel")
        return False