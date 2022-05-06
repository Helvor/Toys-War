import random
import os
from Character import *

class Player:

    def __str__(self):
        return f"Nom : {self.name} | Nombre de vie : {self.life} | Argent : {self.money} | Team : {self.team}"

    def __init__(self, name, life, money):
        self.name = name
        self.life = life
        self.money = money
        self.team = []
        self.game = None
        self.direction = None

    @property
    def is_alive(self):
        return self.life > 0

    def get_hit(self, damages):
        self.life -= damages

    def new_character(self):
        try:
            line = input(f"{self.name}: Wich line would you place the new one (0-{self.game.nb_lines - 1}) ? (enter to pass the turn) ")
            if 0 <= int(line) <= 5:
                for char in available_characters:
                    print(f"{char} - {available_characters[char]}")
                char_choice = input(f"{self.name} : Wich Character do you want to buy ? ")
            if line != "":
                line = int(line)
                if 0 <= line <= self.game.nb_lines - 1:
                    if self.money >= Character.base_price:
                        column = 0 if self.direction == +1 else self.game.nb_columns - 1
                        if char_choice == "F" or char_choice == "f":
                            Fighter(self, (line,column))
                        elif char_choice == "T" or char_choice == "t":
                            Tank(self, (line, column))
                        elif char_choice == "D" or char_choice == "d":
                            Duck(self, (line,column))
        except ValueError:
            pass

class IA(Player):

    def new_character(self):
        os.system('cls')
        print(f"----{int(self.game.nb_columns-len('IA TURN')/2) * '-'}IA TURN{int(self.game.nb_columns-len('IA TURN')/2) * '-'}----")
        line = random.randrange(0, self.game.nb_lines - 1)
        char_choice = random.choice('FTD')
        if self.money >= Character.base_price:
            column = 0 if self.direction == +1 else self.game.nb_columns - 1
            if char_choice == "F":
                Fighter(self, (line, column))
            elif char_choice == "T":
                Tank(self, (line, column))
            elif char_choice == "D":
                Duck(self, (line, column))
