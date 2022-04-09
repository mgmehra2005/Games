games_list = ["1. Snake Water Gun",
              "2. Master Gusser"]
for games in games_list:
    print(games)
user_choice = int(input("\nWhich game you want to play : "))
if (user_choice == 1):
    import games.swg
elif (user_choice == 2):
    import games.Master_Gusser