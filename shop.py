def Shop(money):
    choice = "frogs"
    print()
    print("------------------------------")
    print("Welcome to the shop!")
    while choice != "quit":
        print()
        print("You have", money, "dollars.")
        print("1 to buy potion($10), 2 to buy cupcake ($20), 3 to buy sword ($50), type quit")
        choice = input("enter your choice:")
        if choice == "1":
            if money >= 10:
                print("you bought a potion!")
                money -= 10
            else:
                print("sorry, you don't have enough money!")
        elif choice == "2":
            print("you
#unfinished
