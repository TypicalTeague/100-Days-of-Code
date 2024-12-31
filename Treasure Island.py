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
print("Your mission is to find the treasure")
decisionOne = input("You come to a crossroads.\n"
                    "While the left looks treacherous, dark, and spooky"
                    " the right is bright, sunny, and appears to be safe.\n"
                    "Type 'left' or 'right' to choose your path.")
if decisionOne.lower() == "left":
    print("Congratulations you've chosen a life of adventure. The treasure you seek lies further ahead, will you succeed in getting it. Only time will tell.")
    decisionTwo = input("After venturing further into the island you begin to feel tired.\n"
                        "You know the treasure lies just ahead of you and all you need to do is swim across a lake to a floating piece of land in the middle.\n"
                        "Type 'wait' to sleep until nightfall or 'swim' to go for the treasure now.")
    if decisionTwo.lower() == "wait":
        print("Your decision proves to be a beneficial one.\n"
              "With the moonlight now shining on the lake you see the water is actually quite acidic and melts anything that touches it.\n"
              "While thinking of a plan to cross you are visited by 3 ghosts and each says they can help you cross the lake.\n"
              "While deciphering which one could be telling the truth all you can ascertain from the ghosts are their name.")
        finalDecision = input("The ghosts names are Gold, Brave, and Fear.\n"
                             "With no further hints your final decision lies ahead of you."
                              "Type the name of the ghost you wish to follow 'fear', 'brave', 'gold.")
        if finalDecision.lower() == 'gold':
            print("As if it couldn't be more obvious, you follow the ghost with the name of which you seek.\n"
                  "He lifts you up in one swoop and flies you straight to the center of the island where lies a pile of gold and treasure beyond your wildest dreams.\n"
                  "Congratulations player you have won... Now how do you get back.\n"
                  "The End?")
        elif finalDecision.lower() == 'brave':
            print("The ghost gives you a great big smile. He whisks you away far from the island and all of sudden you find yourself in the middle of a battlefield.\n"
                  "The brave have no need for physical treasures, but instead must seek glory with sword and shield in hand.\n"
                  "Whether you believe the ghost is right or not doesn't matter anymore. Theres no way back and you are stuck in a war of which you know nothing about.\n"
                  "YOU LOSE!!!")
        else:
            print("Whether you chose fear or not it's clear you are not ready for the treasure. The ghost in a sweet delicate smile, pick you up and sooth you to sleep.\n"
                  "This adventure has been a long one and it's time for it all to just end\n"
                  "Before you realize it you have fallen into a deep slumber, never to awaken again.\n"
                  "YOU LOSE!!!")
    elif decisionTwo.lower() == 'swim':
        print("After traveling all day and with the treasure so close, you feel a newfound determination to grab the treasure right now in this moment.\n"
              "You jump into the lake ready to face any further challenges that lie ahead only for your body to melt away and become one with the lake.\n"
              "While you were ready for any challenges ahead, it appears an acid lake was not one of them.\n"
              "YOU LOSE!!!")
    else:
        print("Your own indecisiveness leaves you standing out in the open, and attracts the attention of some dangerous creatures.\n"
              "Still pondering your decision you feel your legs give from under you and are dragged back into the forest never to be seen again.\n"
              "YOU LOSE!!!")
elif decisionOne.lower() == 'right':
    print("Seems the adventuring life is not for you.\n"
          "Treasure does not lie where there's no danger. YOU LOSE!!!")
else:
    print("Seems you've chosen to be a trailblazer and go down your own path.\n"
          "Sadly your treasure map doesn't reward you for creativity.\n"
          "You continually walk in circles until you collapse from exhaustion. YOU LOSE!!!")


