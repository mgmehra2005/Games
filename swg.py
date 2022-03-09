#Snake Water Gun

import random

print("""Snake Water Gun
V.1.1""")

options = ["Snake", "Water", "Gun"]
u_options = ["s","G","W"]
print("""\nInstructions

    (S) for Snake
    (W) for Water
    (G) for Gun""")
t=10
n=1
u = 0
c = 0
while (n<=t):
        print(f"\n{n}.")
        user=input("\nEnter the option : ")
        computer = random.choice(options)
        if (computer == "Snake") and (user == "S"):
            print(f"\nYou : Snake")
            print(f"Computer : Snake")
            print("\nDraw")
            n+=1
            t+=1
        elif (computer == "Snake") and (user == "W"):
            print(f"\nYou : Water")
            print(f"Computer : Snake  +1")
            c+=1
            n+=1
        elif (computer == "Snake") and (user == "G"):
            print(f"\nYou : Gun +1")
            print(f"Computer : Snake")
            u+=1
            n+=1
        elif (computer == "Water") and (user == "W"):
            print(f"\nYou : Water")
            print(f"Computer : Water")
            print("\nDraw")
            n+=1
            t+=1
        elif (computer == "Water") and (user == "S"):
            print(f"\nYou : Snake +1")
            print(f"Computer : Water")
            u+=1
            n+=1
        elif (computer == "Water") and (user == "G"):
            print(f"\nYou : Gun")
            print(f"Computer : Water +1")
            c+=1
            n+=1
        elif (computer == "Gun") and (user == "G"):
            print(f"\nYou : Gun")
            print(f"Computer : Gun")
            print("\nDraw")
            n+=1
            t+=1
        elif (computer == "Gun") and (user == "S"):
            print(f"\nYou : Snake")
            print(f"Computer : Gun +1")
            c+=1
            n+=1
        elif (computer == "Gun") and (user == "W"):
            print(f"\nYou : Water +1")
            print(f"Computer : Gun")
            u+=1
            n+=1
        elif (user != u_options):
            print("You have entered wrong value. Try again.")
            continue
print(f"""\n-------------------
| Computer | User |
-------------------
|   {c}      |   {u}  |
-------------------""")
if u > c:
    print("\n YOU WON")
elif u==c:
    print("\nDraw")
else:
    print("\n YOU LOOSE")