print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
answer = input("\nYou're at a cross road. Where do you want to go ? Type 'left' or 'right'\n").lower()
if (answer == "left"):
    answer = input("\nYou have come to a lake. There is a island in the middle of the lake.\n\nType 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if (answer == 'wait'):
        answer = input('\nYou arrived at the island uunharmed. There is house with 3 doors. One red, one yellow, one blue. Which one do you choose? \n' ).lower()
        if (answer == 'red'):
            print("\nIt's a rooom full of fire. Game Over. \n")
        elif (answer == 'yellow'):
            print("\nYou found the tresure. You Win !\n")
        elif (answer == 'blue'):
            print("\nYou enter a room of beasts. Game Over. \n")
        else : 
            print("\nYou choose a door that doesn't exist. Game Over. \n")

    elif (answer == 'swim'):
        print("You got attacked by a angry trout. Game Over. \n")
elif(answer == "right"):
    print("you fell in a hole. Game Over. \n")