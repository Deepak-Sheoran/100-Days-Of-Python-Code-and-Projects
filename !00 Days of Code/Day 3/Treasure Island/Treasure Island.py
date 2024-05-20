from Logo import logo
print(logo)
print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
choice1 = input('You are at a cross road. Where do you want to go? Type "left" or "right" = ')
if choice1.lower() == "left":
    choice2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a '
                    'boat. Type "swim" to swim across = ')
    if choice2.lower() == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house with three doors. One red, one yellow '
                        'and one blue. Which color do you choose? = ')
        if choice3.lower() == "yellow":
            print("You enter the room with the treasure chest. You Win!!")
        else:
            print("You enter a room full of beasts. You Lose!!")
    else:
        print("You drown while trying to reach the island. You Lose!!")
else:
    print("Wrong choice, you wander around unable to find the treasure, You Lose!!")
