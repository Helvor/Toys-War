from Character import *
from Player import *
from Game import *


if __name__ == "__main__":
    exit = ""
    while not exit == "Q" or not exit == "q":
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
        choice_game = int(input("Game mode choice : "))
        if choice_game == 0:
            exit = "Q"
        elif choice_game == 1:
            player1 = Player(input("Player 1 : "), 20, 10)
            player2 = Player(input("Player 2 : "), 20, 10)
            game = Game(player1, player2)
            game.play()
            if player1.life <= 0:
                print(f"Great Job {player2.name} ! You won the game")
            elif player2.life <= 0:
                print(f"Great Job {player1.name} ! You won the game")

            exit = input("Enter for returning to the menu : ")

        elif choice_game == 2:
            player1 = IA("IA", 20, 10)
            player2 = Player(input("Player 1 : "), 20, 10)
            game = Game(player1, player2)
            game.play()
            if player1.life <= 0:
                print(f"L'IA à gagné ! :(")
            elif player2.life <= 0:
                print(f"Great Job {player1.name} ! You won the game")

            exit = input("Enter for returning to the menu : ")
