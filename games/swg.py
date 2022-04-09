#Snake Water Gun
'''It is an silly game for timepass. Here computer will play with you.'''

#Imported Modules
import random

#Program Start
print(""" ____              _      __        __    _             ____
/ ___| _ __   __ _| | ____\ \      / __ _| |_ ___ _ __ / ___|_   _ _ __
\___ \| '_ \ / _` | |/ / _ \ \ /\ / / _` | __/ _ | '__| |  _| | | | '_ \\
 ___) | | | | (_| |   |  __/\ V  V | (_| | ||  __| |  | |_| | |_| | | | |
|____/|_| |_|\__,_|_|\_\___| \_/\_/ \__,_|\__\___|_|   \____|\__,_|_| |_| V.1.2""")           #Header

computer_options = ["Snake", "Water", "Gun"]
user_options = ["s","G","W"]
print("""\nInstructions

    (S) for Snake
    (W) for Water
    (G) for Gun""")
total_chance=10
counting=1
user_score = 0
computer_score = 0
while (counting <= total_chance):

        print(f"\n{counting}.")
        user_input = input("\nEnter the option : ")
        computer = random.choice(computer_options)

        if (computer == "Snake") and (user_input == "S"):
            print(f"\nYou : Snake")
            print(f"Computer : Snake")
            print("\nDraw")
            counting += 1
            total_chance += 1

        elif (computer == "Snake") and (user_input == "W"):
            print(f"\nYou : Water")
            print(f"Computer : Snake  +1")
            computer_score += 1
            counting += 1

        elif (computer == "Snake") and (user_input == "G"):
            print(f"\nYou : Gun +1")
            print(f"Computer : Snake")
            user_score += 1
            counting += 1

        elif (computer == "Water") and (user_input == "W"):
            print(f"\nYou : Water")
            print(f"Computer : Water")
            print("\nDraw")
            counting += 1
            total_chance += 1

        elif (computer == "Water") and (user_input == "S"):
            print(f"\nYou : Snake +1")
            print(f"Computer : Water")
            user_score += 1
            counting += 1

        elif (computer == "Water") and (user_input == "G"):
            print(f"\nYou : Gun")
            print(f"Computer : Water +1")
            computer_score += 1
            counting += 1

        elif (computer == "Gun") and (user_input == "G"):
            print(f"\nYou : Gun")
            print(f"Computer : Gun")
            print("\nDraw")
            counting += 1
            total_chance += 1

        elif (computer == "Gun") and (user_input == "S"):
            print(f"\nYou : Snake")
            print(f"Computer : Gun +1")
            computer_score += 1
            counting += 1
        elif (computer == "Gun") and (user_input == "W"):
            print(f"\nYou : Water +1")
            print(f"Computer : Gun")
            user_score += 1
            counting += 1
        elif (user_input != user_options):
            print("You have entered wrong value. Try again.")
            continue

print(f"""\n-------------------
| COMPUTER | YOU  |
-------------------
|   {computer_score}      |   {user_score}  |
-------------------""")             #Score Board

if (user_score > computer_score):
    print("\n YOU WON")

elif (user_score == computer_score):
    print("\nDraw")

else:
    print("\n YOU LOOSE")
#Program end