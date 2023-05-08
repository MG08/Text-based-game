inventory = ["","","","",""]
room = 1
choice = "hi"
print("welcome to the text based game!")

while choice != "quit": #game loop------------------------------------
    if room == 1:
        choice = input("There's a door in front of you. Enter it?")
        if choice == "Yes" or choice == "yes":
            room = 2
        if choice == "No" or choice == "no":
            print("You stay in the room, still followed with the ominous silence. Nothing out of the ordinary in this room. Only thing to do is going through the door.")
        else:
            print("Type something that makes sense")
            
    elif room == 2:
        choice = input("You enter the room...There's nothing out of the ordinary in this room either, except those weird dark humanid looking statues beside each other... You can either enter the left door or the right door in this room. Which one do you want to enter?")
        if choice == "Back" or choice == "back":
            room = 1
        if choice == "Right" or choice == "right":
            if inventory[0] == "key":
                print("The door unlocks, you go in...")
            room = 3
            elif inventory[0] != "key":
                print("The door doesn't budge, it looks like it's locked.")
        if choice == "Left" or choice == "left":
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
        choice = input("You enter the room, a large clock on the left with a door on the right. There’s a window right in front of you. Enter the right door?(You can go back)")
        if choice == "Right" or choice == "right":
            room = 6
        if choice == "Back" or choice == "back":
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
