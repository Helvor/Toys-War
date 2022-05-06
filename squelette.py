from Character import *
from Player import *
from Game import *


if __name__ == "__main__":
    print("""
 _____                   __    __           
/__   \___  _   _ ___   / / /\ \ \__ _ _ __ 
  / /\/ _ \| | | / __|  \ \/  \/ / _` | '__|
 / / | (_) | |_| \__ \   \  /\  / (_| | |   
 \/   \___/ \__, |___/    \/  \/ \__,_|_|   
            |___/                           """)
    player1 = Player(input("Nom joueur 1 : "), 20, 10)
    player2 = Player(input("Nom joueur 2 : "), 20, 10)
    game = Game(player1, player2)
    game.play()
    if player1.life <= 0:
        print(f"Bravo {player2.name}")
    elif player2.life <= 0:
        print(f"Bravo {player1.name}")

    exit = input("Veuillez quitter la fenetre")
