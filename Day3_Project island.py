print("Welcome to treasure island.")
print("your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? type "left" or "right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. type "wait" to wait for a boat. type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input ("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()

        if choice3 == "red":
           print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
        
        else: 
          print("You chose a door that doesn't exist. Game over.")
    else:
       print("You got atttacked by an angry trout. Game over. SAYO")

else:
    print("You fell into a hole. Game over")

