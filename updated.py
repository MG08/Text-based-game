inventory = ["","","","",""]
room = 1
choice = "hi"
print("welcome to the text based game!")

while choice != "quit": #game loop------------------------------------
    if room == 1:
        choice = input("You are in room 1. You can go East. ")
        if choice == "East" or choice == "east":
            room = 2
        else:
            print("I don't understand that.")
            
    elif room == 2:
        choice = input("You are in room 2. You can go West, South, or North")
        if choice == "West" or choice == "west":
            room = 1
        if choice == "South" or choice == "south":
            room = 3
        if choice == "North" or choice == "north":
            room = 4
        else:
            print("I don't understand that.")
            
    elif room == 3:
        choice = input("You are in room 3. You can go North or East. ")
        if choice == "North" or choice == "north":
            room = 2
        if choice == "East" or choice == "east":
            room = 5
        else:
            print("I dont understand that.")
            
    elif room == 4:
        choice = input("You are in room 4. You can go South or East.")
        if choice == "East" or choice == "east":
            room = 6
        if choice == "South" or choice == "south":
            room = 2
        else:
            print("I don't understand that.")
            
    elif room == 5:
        choice = input("You are in room 5. You can go West or East.")
        if choice == "East" or choice == "east":
            room = 8
        if choice == "West" or choice == "west":
            room = 3
        else:
            print("I don't understand that.")
            
    elif room == 6:
        choice = input("You are in room 6. You can go West or East.")
        if choice == "West" or choice == "west":
            room = 4
        if choice == "East" or choice == "east":
            room = 7
        else:
            print("I don't understand that.")
            
    elif room == 7:
        choice = input("You are in room 7. You can go West or South.")
        if choice == "West" or choice == "west":
            room = 6
        if choice == "South" or choice == "south":
            room = 10
        else:
            print("I don't understand that.")
            
    elif room == 8:
        choice = input("You are in room 8. You can go West, North, or South.")
        if choice == "West" or choice == "west":
            room = 5
        if choice == "South" or choice == "south":
            room = 9
        if choice == "North" or choice == "north":
            room = 10
        else:
            print("I don't understand that.")
            
    elif room == 9:
        choice = input("You are in room 9. You can go North or South")
        if choice == "North" or choice == "north":
            room = 8
        if choice == "South" or choice == "south":
            room = 11
        else:
            print("I don't understand that.")
            
    elif room == 10:
        choice = input("You are in room 10. You can go North, East, or South.")
        if choice == "East" or choice == "east":
            room = 12
        if choice == "South" or choice == "south":
            room = 8
        if choice == "North" or choice == "north":
            room = 7
            
    elif room == 11:
        choice = input("You are in room 11. You can go North.")
        if choice == "North" or choice == "north":
            room = 9
            
    elif room == 12:
        choice = input("You are in room 12. You can go West or East.")
        if choice == "West" or choice == "west":
            room = 10
        if choice == "East" or choice == "east":
            room = 13
            
    elif room == 13:
        choice = input("You are in room 13. You can go West.")
        if choice == "West" or choice == "west":
            room = 12
        
#end pf game loop
print("Thanks for playing. Goodbye.")
