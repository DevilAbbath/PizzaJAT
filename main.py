import time
from menu import showmenu
from makepizza import doughtype, saucetype, modifyingt, showpizza
from estimated import esttime, confirm

def main():
    dough = "Traditional"
    sauce = "Tomato"
    ingredients = []

    while True:
        showmenu()
        print("Default Pizza, Traditional dought and Tomato Sauce.")
        option = int(input("\nSelect an option (1-7): "))
        
        if option == 1:
            dough = doughtype()
            time.sleep(3)
        elif option == 2:
            sauce = saucetype()
            time.sleep(3)
        elif option == 3:
            ingredients = modifyingt(ingredients)
            time.sleep(3)
        elif option == 4:
            showpizza(dough, sauce, ingredients)
            time.sleep(3)
        elif option == 5:
            ttotal = esttime(ingredients)
            time.sleep(3)
        elif option == 6:
            ttotal = esttime(ingredients)
            if confirm(dough, sauce, ingredients, ttotal):
                break
        elif option == 7:
            print ("Exiting without confirm order...")
            break
        else:
            print ("Please select an valid option.")
            time.sleep(5)

if __name__ == "__main__":
    main()