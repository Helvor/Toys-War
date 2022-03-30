

class Player :

    def __str__(self):
        return f"Nom : {self.name} | Nombre de vie : {self.life} | Argent : {self.money} | Team : {self.team}"

    def __init__(self, name, life, money):
        """
        PARAM : - name : str
                - life : float
                - money : float
        initialisate team to empty list, game and direction to None
        """
        self.name = str(name)
        self.life = float(life)
        self.money = float(money)
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
        self.damages = damages
        return self.life - damages


    def new_character(self):
        """
        Ask to player where add a new Character,
        check if enough money
        and create the new one
        """
        line = input(f"{self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
        if line != "":
            line = int(line)
            if 0<=line<=self.game.nb_lines-1 :
                if self.money >= Character.base_price :
                    column = 0 if self.direction == +1 else self.game.nb_columns-1
                    Character(self,(line,column))


class Game :

    def __init__(self, player0, player1, nb_lines=6,nb_columns=15):
        """
        PARAM : - player0 : Player
                - player1 : Player
                - nb_lines : float
                - nb_columns : float
        - update player's direction and game
        - initialisate player_turn to 0
        """
        self.nb_lines = int(nb_lines)
        self.nb_columns = int(nb_columns)
        self.players = [player0,player1]
        self.player_turn = int(0)

        self.players[0].game = self
        self.players[1].game = self
        self.players[0].direction = 1
        self.players[1].direction = -1

    @property
    def current_player(self):
        self.player_turn += 1
        if self.player_turn %2 != 0:
            return self.players[0]
        elif self.player_turn %2 == 0:
            return self.players[1]


    @property
    def oponent(self):
        self.player_turn += 1
        if self.player_turn % 2 != 0:
            return self.players[1]
        elif self.player_turn % 2 == 0:
            return self.players[0]


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




    def draw(self):
        """
        print the board
        """
        print(f"{self.players[0].life:<4}{'  '*self.nb_columns}{self.players[1].life:>4}")

        print("----"+self.nb_columns*"--"+"----")

        for line in range(self.nb_lines):
            print(f"|{line:>2}|", end="")
            for col in range(self.nb_columns):
                # TODO
                print(".", end=" ")
            print(f"|{line:<2}|")

        print("----"+self.nb_columns*"--"+"----")

        print(f"{self.players[0].money:<3}${'  '*self.nb_columns}${self.players[1].money:>3}")


    def play_turn(self):
        """
        play one turn :
            - current player can add a new character
            - current player's character play turn
            - oponent player's character play turn
            - draw the board
        """
        # TODO



    def play(self):
        """
        play an entire game : while current player is alive, play a turn and change player turn
        """
        # TODO






### PERSONNAGES ###
class Character :

    base_price = 1
    base_life = 5
    base_strength = 1 

    def __init__(self, player, position):
        """
        PARAM : - player : Player
                - position : tuple
        Set player to player in param.
        Set life, strength and price to base_life, base_strength and base_price.
        Place th character at the position
        If OK : add the current character to the player's team and take the price
        """

        self.player = player
        self.life = self.base_life
        self.strength = self.base_strength
        self.price = self.base_price

        ok = self.game.place_character(self, position)
        if ok :
            self.player.team.append(self)
            self.player.money -= self.price


    @property
    def direction(self):
        """
        self.player[0] = 1
        self.player[1] = -1
        return self.player[0] and self.player[1]
        """
        if self.player[0]:
            return self.player[0].direction = 1
        elif self.player[1]:
            return self.player[1].direction = -1

    @property
    def game(self):
        return self.game

    @property
    def enemy(self):
        """
        self.ennemy[0] = self.player[1]
        self.ennemy[1] = self.player[0]
        return self.ennemy[0] and self.ennemy[1]
        """
        if self.player[0]:
            self.enemy[0] = self.player[1]
        elif self.player[1]:
            self.enemy[1] = self.player[0]


    @property
    def design(self):
        self.player[0].design = ">"
        self.player[1].design = "<"
        return self.player[0].design and self.player[1].design


    def move(self):
        """
        the character move one step front
        """
        # TODO


    def get_hit(self, damages):
        """
        Take the damage to life. If dead, the character is removed from his team and return reward
        PARAM : damages : float
        RETURN : the reward due to hit (half of price if the character is killed, 0 if not)
        """
        # TODO


    def attack(self):
        """
        Make an attack :
            - if in front of ennemy's base : hit the base
            - if in front of character : hit him (and get reward)
        """
        # TODO


    def play_turn(self):
        """
        play one turn : move and attack
        """
        # TODO


    def __str__(self):
        """
        return a string represent the current object
        """
        # TODO





if __name__ == "__main__":
    print("Let's Play !!! ")
    # TODO
    zozo = Player("zozo", 30, 74)
    lolo = Player("lolo", 25, 10)
    game = Game(zozo, lolo)
    print(f"{zozo.__str__()}\n{lolo.__str__()}")
    print(game.get_character_at([3, 5]))
   
