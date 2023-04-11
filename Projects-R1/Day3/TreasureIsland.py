print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.
# drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

option1 = input("You have encountered two doors. which one do you want to pick ? Type 'left' of 'right'\n").lower()

if option1 != "left":
    print("Unlucky choice, the door was trapped and now you are dead. Game Over")
else:
    option2 = input("You see a nice pool and it is a hot day. What do you want to do ? Type 'swim' or 'wait'\n").lower()

    if option2 != "wait":
        print("The pool was full of piranhas. You were eaten alive. Game Over")
    else:
        option3 = input("You have three coloured doors. which one do you want to pick ? Type 'red' "
                        ", 'blue' , 'yellow '\n").lower()

        if option3 == "red":
            print("You were burned by fire. Game Over")
        elif option3 == "blue":
            print("Eaten by Beasts. Game Over")
        elif option3 == "yellow":
            print("Congratulations. You win!")
        else:
            print("You suck at this game. Game Over")


