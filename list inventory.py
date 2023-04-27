inventory = ["","","","",""]
room = 1
while True:
    if room == 1:
        print("You're in room 1, you can go south")
        choice = input()
        if choice == "south":
            room = 2
    if room == 2:
        print("You're in room 2, you can go south or north")
        if inventory[0]!="key":
            print("You see a key on the floor!")
        choice = input()
        if choice == "south":
            room = 3
        if choice == "north":
            room = 1
        if choice == "get key" or choice == "key":
            inventory[0]="key"
            
    if room == 3:
        print("You're in room 3, you can go east or north")
        print("You see a rug on the floor")
        choice = input()
        if choice == "east":
            if inventory[0]=="key":
                print("You open the door with the key")
                inventory[0] = ""
                room = 4
        if choice == "north":
            room = 2
        if choice == "rug" or choice == "look under rug":
            if inventory[1] != "sword":
                inventory[1]="sword"
                print("You find a sword and pick it up")
            else:
                print("There is only dust under the rug.")
            
    if room == 4:
        print("You're in room 4, you can go west")
        if inventory[1]=="sword":
            print("A dragon appears and you kill it, then escape")
        else:
            print("You get eaten by the dragon")
        choice = input()
        if choice == "west":
            room = 3
