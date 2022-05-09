from Character import *
from Player import *
from Game import *

if __name__ == "__main__":
    action_prog = ""
    while not action_prog == "Q":
        print("""
     _____                   __    __           
    /__   \___  _   _ ___   / / /\ \ \__ _ _ __ 
      / /\/ _ \| | | / __|  \ \/  \/ / _` | '__|
     / / | (_) | |_| \__ \   \  /\  / (_| | |   
     \/   \___/ \__, |___/    \/  \/ \__,_|_|   
                |___/                           """)
        print("Welcome in -TOYS WAR- || a game coded in python\n"
              "Available game mode :\n"
              "1 - Player vs Player\n"
              "2 - Player vs IA\n"
              "0 - Quit")
        choice_game = input("Game mode choice : ")
        verif = choice_game.isnumeric()
        while not verif:
            choice_game = input("(entrez un nombre) Game mode choice : ")
            verif = choice_game.isnumeric()
            while not choice_game == range(0,2):
                choice_game = input("(entrez un nombre entre 0, 1 et 2) Game mode choice : ")
        choice_game = int(choice_game)
        if choice_game == 0:
            action_prog = "Q"
        elif choice_game == 1:
            print("""
  _____  _            __     ________ _____   _____   _   _          __  __ ______ 
 |  __ \| |        /\ \ \   / /  ____|  __ \ / ____| | \ | |   /\   |  \/  |  ____|
 | |__) | |       /  \ \ \_/ /| |__  | |__) | (___   |  \| |  /  \  | \  / | |__   
 |  ___/| |      / /\ \ \   / |  __| |  _  / \___ \  | . ` | / /\ \ | |\/| |  __|  
 | |    | |____ / ____ \ | |  | |____| | \ \ ____) | | |\  |/ ____ \| |  | | |____ 
 |_|    |______/_/    \_\|_|  |______|_|  \_\_____/  |_| \_/_/    \_\_|  |_|______|\n""")
            player1 = Player(input("Player 1 : "), 20, 10)
            player2 = Player(input("Player 2 : "), 20, 10)
            os.system('cls')
            game = Game(player1, player2)
            game.play()
            if player1.life <= 0:
                print("""
 __     ______  _    _  __          _______ _   _
 \ \   / / __ \| |  | | \ \        / /_   _| \ | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |
    |_|  \____/ \____/      \/  \/   |_____|_| \_|\n"""
                      f"Great Job {player2.name} ! You won the game")
            else:
                print("""
 __     ______  _    _  __          _______ _   _
 \ \   / / __ \| |  | | \ \        / /_   _| \ | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |
    |_|  \____/ \____/      \/  \/   |_____|_| \_|\n"""
                      f"Great Job {player1.name} ! You won the game")

            action_prog = input("Enter for returning to the menu : ")
            os.system('cls')

        elif choice_game == 2:
            player1 = IA("IA", 20, 10)
            player2 = Player(input("Player 1 : "), 20, 10)
            os.system('cls')
            game = Game(player1, player2)
            game.play()
            if player2.life <= 0:
                print("""
 __     ______  _    _   _      ____   _____ ______
 \ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__
   \   /| |  | | |  | | | |   | |  | |\___ \|  __|
    | | | |__| | |__| | | |___| |__| |____) | |____
    |_|  \____/ \____/  |______\____/|_____/|______|\n"""
                      "IA won ! :(")
            elif player1.life <= 0:
                print("""
 __     ______  _    _  __          _______ _   _
 \ \   / / __ \| |  | | \ \        / /_   _| \ | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |
    |_|  \____/ \____/      \/  \/   |_____|_| \_|\n"""
                      f"Great Job {player1.name} ! You won the game")

            action_prog = input("Enter for returning to the menu : ")
            os.system('cls')
