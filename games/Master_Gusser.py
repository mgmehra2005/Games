'''It is an silly game for timepass.'''

#Imported module
import random

#Program start
print(""" __  __           _             ____
|  \/  | __ _ ___| |_ ___ _ __ / ___|_   _ ___ ___  ___ _ __
| |\/| |/ _` / __| __/ _ | '__| |  _| | | / __/ __|/ _ | '__|
| |  | | (_| \__ | ||  __| |  | |_| | |_| \__ \__ |  __| |
|_|  |_|\__,_|___/\__\___|_|   \____|\__,_|___|___/\___|_| V.1.1""")
name = input("\nEnter your name : ")
print(f'\nHello {name}')
print("\nLet's start the game.")
print("\n* You have only 10 Chance.")

hidden_number = random.randrange(1, 100)
count = 1
chance_limit = 10

while count <= chance_limit:
    user_input = int(input(f"\n({count}) Enter Value : "))
    count = count + 1

    if user_input == hidden_number:
        print("\nVictory")
        break
    elif user_input >= hidden_number - 10 and user_input <= hidden_number + 10:
        print("\nYou are very close.")
    else:
        print('\nWrong')
print(f"\nHidden Number : {hidden_number}")
#Program end