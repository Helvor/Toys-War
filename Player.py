from Character import *

class Player:

    def __str__(self):
        return f"Nom : {self.name} | Nombre de vie : {self.life} | Argent : {self.money} | Team : {self.team}"

    def __init__(self, name, life, money):
        """
        PARAM : - name : str
                - life : float
                - money : float
        initialisate team to empty list, game and direction to None
        """
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
        """
        Take the damage to life
        PARAM : - damages : float
        """
        self.life -= damages

    def new_character(self):
        """
        Ask to player where add a new Character,
        check if enough money
        and create the new one
        """
        buy_choice = input(f"{self.name} : Do you want to buy this turn (Y/N) ? (or enter if no) ")
        if buy_choice == "y" or buy_choice == "Y":
            line = input(f"{self.name}: Wich line would you place the new one (0-{self.game.nb_lines - 1}) ?")
            print(f"List of character : \n"
                  f"F - Fighter : {Character.__str__(Fighter)}\n"
                  f"T - Tank : {Character.__str__(Tank)}\n"
                  f"D - Duck : {Character.__str__(Duck)}")
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
