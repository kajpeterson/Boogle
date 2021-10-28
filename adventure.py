#Make sure to have a big enough terminal so that the player can see the phrase, "You can't go any further in that direction."
#Full screen on the Air, that's 2ish rows about the top of the title.

def map(X,Y):
#Prints a map, depending on the coordinates
    if X == 1 and Y == 1: 
        print("\n________________\n|    |    |    |\n|              |\n_    __   __   _\n|    |    |    |\n| X            |\n________________\n")
    if X == 2 and Y == 1: 
        print("\n________________\n|    |    |    |\n|              |\n_    __   __   _\n|    |    |    |\n|      X       |\n________________\n")
    if X == 3 and Y == 1: 
        print("\n________________\n|    |    |    |\n|              |\n_    __   __   _\n|    |    |    |\n|           X  |\n________________\n")
    if X == 1 and Y == 2: 
        print("\n________________\n|    |    |    |\n| X            |\n_    __   __   _\n|    |    |    |\n|              |\n________________\n")
    if X == 2 and Y == 2: 
        print("\n________________\n|    |    |    |\n|      X       |\n_    __   __   _\n|    |    |    |\n|              |\n________________\n")
    if X == 3 and Y == 2: 
        print("\n________________\n|    |    |    |\n|           X  |\n_    __   __   _\n|    |    |    |\n|              |\n________________\n")



def locator(X,Y):
#translates coordinates to room number
    if X ==1 and Y ==1:
        room = 1
    if X ==2 and Y ==1:
        room = 2
    if X ==3 and Y ==1:
        room = 3
    if X ==1 and Y ==2:
        room = 4
    if X ==2 and Y ==2:
        room = 5
    if X ==3 and Y ==2:
        room = 6
    return room



def move(key,Map,X,Y):
#translate move command into coordinate change
    if key == "w":
        Y = Y+1
    elif key == "a":
        X = X-1
    elif key == "s":
        Y = Y-1
    elif key == "d":
        X = X+1
#checks whether boundaries have been crossed
    if X == 0:
        print("\n\nYou can't go any further in that direction.")
        X = 1
    elif X == 4:
        print("\n\nYou can't go any further in that direction.")
        X = 3
    if Y == 0:
        print("\n\nYou can't go any further in that direction.")
        Y = 1
    if Y == 3:
        print("\n\nYou can't go any further in that direction.")
        Y = 2            
#Show map if you have it    
    if 1 <= X <= 3 and 1 <= Y <= 2:
        if Map == 1:
            map(X,Y)
    return (X, Y)



def describe(room):
#Describes what the room looks like and what's in it
    print("\n")
    if room == 1:
        print("You are in the Throne Room. The room is made of stone and ornately decorated with gold candelabras and red carpet. A wooden throne sits vacant by the wall.\nAt its feet, a prince is slumped on the floor.")
    if room == 2:
        print("You are in the Armory. Swords and Armor line the stone walls. You wouldn't think chain mail would hold a stench, but you'd be wrong!")
    if room == 3:
        print("You are in the Messy Room. I guess this is where everyone throws their crap. It's hard to make your way through the piles of things big and small.")
    if room == 4:
        print("You are in the Kitchen. A ceramic wash basin by the wall is all dried up. The wood-burning stove is cold. A wooden chest by the other wall is covered in dust.")
    if room == 5:
        print("You are in the Library. Books line the walls. You know the Prince hasn't read half of these. A mess of papers is sprawled across the table top.")
    if room == 6:
        print("You are in the Bedroom. Curtains hang from a wooden frame surrounding an empty bed in the middle of the room, surrounded by ornate carpets.")
    print("\n")


def action(room,Map,Key,Water,Win,X,Y):
#This function defines what happens when the player hits z
#Depends on which room you're in and which objects you have
    if room == 1:
        #print("Room 1 entered")
        if Water == 1:
            print("You open the flask and press it to the Prince's lips. He drinks it and feels way better. Dude was just a lil dehydrated, that's all!")
            Win = 1
        else:
            print("You lean down and touch the prince on his shoulder. 'I'm so thirsty...', he replies.")
    if room == 2:
        print("Nothing to do here...")
    if room == 3:
        if Key == 1:
            print("Nothing else useful in here...")
        else:
            Key = 1
            print("You rummage through the piles of crap. Your hand touches something cold and hard.\nYOU FOUND A KEY!\nBetter hold on to this just in case. ;)")
    if room == 4:
        if Water == 1:
            print("You've already opened this chest.")
        else:
            if Key == 1:
                Water = 1
                print("You try the key in the chest. The key fits! You turn the key and it unlocks the chest. You open it up and find a flask of water.\nYOU GOT A FLASK OF WATER!")
            else:
                print("You try opening the chest, but it's locked.")
    if room == 5:
        if Map == 1:
            print("Nothing to do here...")
        else:
            Map = 1
            print("YOU FOUND A MAGIC MAP!")
            map(X,Y)
    if room == 6:
        print("Nothing to do here...")
    return (Map,Key,Water,Win)



def check(Map, Key, Water):
#prints a list of objects the player has
    print("You have:")
    if Map == 1:
        print ("A Magic Map")
    if Key == 1:
        print ("A Key")
    if Water == 1:
        print ("A Flask of Water")
    if Map == 0 and Key == 0 and Water == 0:
        print("Nothing :(")



def main():
    print("\n\n\n\n\n-----------------\nADVENTURE GAME!!!\n-----------------\nMove with w,a,s,d.\nz = action\nc = check possessions\nq = quit\n")
    X = 1
    Y = 1
    Map = 0
    Key = 0
    Water = 0
    room = 1
    Win = 0
    describe(room)
    while True:
        key = input("\n---What would you like to do?--- ")
        print("\n")
        if key == "w" or key == "a" or key == "s" or key == "d":
            (X, Y) = move(key,Map,X,Y)
            room = locator(X,Y)
            describe(room)
            continue
        elif key == "z":
            (Map,Key,Water,Win) = action(room,Map,Key,Water,Win,X,Y)
            if Win == 1:
                break
            continue
        elif key =="c":
            check(Map, Key, Water)
            continue
        elif key == "q":
            break
        else:
            print("Not a valid command.\nMove with w,a,s,d.\nz = action\nc = check possessions\nq = quit\n")
    if Win == 0:
        print("GAME OVER")
    elif Win == 1:
        print("\n\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n*    *    *    *    *    *    *    *    *    *\nCongratulations! You saved the thirsty prince!\n*    *    *    *    *    *    *    *    *    *\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n")
main()


#If you want to add more to this game, try:
#   randomizing the location of the objects.
#   using a list & library method of relative locations, instead of coordinates.
#   realizing when the character has already been in a room.
#   stop it from printing room descriptions after every action.
#   adding a tic toc game timer


