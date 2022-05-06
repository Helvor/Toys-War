from Character import *

class Game:

    def __init__(self, player0, player1, nb_lines=6, nb_columns=15):
        """
        PARAM : - player0 : Player
                - player1 : Player
                - nb_lines : float
                - nb_columns : float
        - update player's direction and game
        - initialisate player_turn to 0
        """
        self.nb_lines = nb_lines
        self.nb_columns = nb_columns
        self.players = [player0, player1]
        self.player_turn = 0

        self.players[0].game = self
        self.players[1].game = self
        self.players[0].direction = 1
        self.players[1].direction = -1

    @property
    def current_player(self):
        return self.players[self.player_turn]

    @property
    def oponent(self):
        if self.player_turn == 0:
            self.player_turn = 1
        elif self.player_turn == 1:
            self.player_turn = 0
        return self.players[self.player_turn]

    @property
    def all_characters(self):
        return self.players[0].team + self.players[1].team

    def get_character_at(self, position):
        """
        PARAM : - position : tuple
        RETURN : character at the position, None if there is nobody
        """
        actual_character = None
        for character in self.all_characters:
            if character.position == position:
                actual_character = character
        return actual_character

    def place_character(self, character, position):
        """
        place character to position if possible
        PARAM : - character : Character
                - position : tuple
        RETURN : bool to say if placing is done or not
        """
        if (0, 0) <= position < (self.nb_lines, self.nb_columns):
            if self.get_character_at((position[0], position[1])) == None:
                character.position = position
                return True
            else:
                return False

    def draw(self):
        """
        print the board
        """
        print(f"{self.players[0].name} : {self.players[0].life:<4}♥{' ' * self.nb_columns}♥{self.players[1].life:>4} : {self.players[1].name}")

        print("----" + self.nb_columns * "--" + "----")

        for line in range(self.nb_lines):
            print(f"|{line:>2}|", end="")
            for col in range(self.nb_columns):
                # TODO
                if self.get_character_at((line, col)) == None:
                    print(".", end=" ")
                else:
                    print(self.get_character_at((line, col)).design, end=" ")
            print(f"|{line:<2}|")

        print("----" + self.nb_columns * "--" + "----")

        print(f"{self.players[0].money:<3}${'  ' * self.nb_columns}${self.players[1].money:>3}")

    def play_turn(self):
        """
        play one turn :
            - current player can add a new character
            - current player's character play turn
            - oponent player's character play turn
            - draw the board
        """
        Player.new_character(self.current_player)
        for character in self.current_player.team + self.oponent.team:
            character.play_turn()
        self.draw()

    def play(self):
        """
        play an entire game : while current player is alive, play a turn and change player turn
        """
        while self.current_player.is_alive and self.oponent.is_alive:
            self.play_turn()
            self.player_turn = 1 - self.player_turn

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


class Fighter(Character):
    base_price = 2
    base_life = 7
    base_strength = 3

    def __str__(self):
        return f"{self.name[:1]} - {self.name} : {self.base_price}$ - Force : {self.base_strength} - Life : {self.base_life}"

    @property
    def design(self):
            return '@' if self.direction == 1 else '@'

class Tank(Character):
    base_price = 5
    base_life = 10
    base_strength = 1

    def __str__(self):
        return f"{self.name[:1]} - {self.name} : {self.base_price}$ - Force : {self.base_strength} - Life : {self.base_life}"

    @property
    def design(self):
        return 'O' if self.direction == 1 else 'O'

class Duck(Character):
    base_price = 8
    base_life = 10
    base_strength = 20

    def __str__(self):
        return f"{self.name[:1]} - {self.name} : {self.base_price}$ - Force : {self.base_strength} - Life : {self.base_life}"

    @property
    def design(self):
        return '^' if self.direction == 1 else '^'

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
