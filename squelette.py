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
        line = input(f"{self.name}: Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none)")
        if line != "":
            line = int(line)
            if 0 <= line <= self.game.nb_lines-1:
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
        self.nb_lines = nb_lines
        self.nb_columns = nb_columns
        self.players = [player0,player1]
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
        self.character = character
        if (0,0) <= position <= (self.nb_lines, self.nb_columns):
            if self.get_character_at() == None:
                self.character.position = position
                return True
            else:
                return False
        else:
            return "Erreur : position en dehors du plateau"

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
                if self.get_character_at(col) == None:
                    print(".", end=" ")
                else:
                    print(self.character.design)
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

    def play(self):
        """
        play an entire game : while current player is alive, play a turn and change player turn
        """
        while self.current_player.is_alive :
            self.play_turn()

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
        return self.player.direction

    @property
    def game(self):
        return self.player.game

    @property
    def enemy(self):
        return self.game.oponent

    @property
    def design(self):
        return '>' if self.direction() == 1 else '<'

    def move(self):
        """
        the character move one step front
        """
        self.position += self.direction
        self.game.place_character()

    def get_hit(self, damages):
        """
        Take the damage to life. If dead, the character is removed from his team and return reward
        PARAM : damages : float
        RETURN : the reward due to hit (half of price if the character is killed, 0 if not)
        """
        self.life -= damages
        reward = 0
        if self.life <= 0:
            self.player.team.remove(self)
            reward = self.price / 2
        return reward


    def attack(self):
        """
        Make an attack :
            - if in front of ennemy's base : hit the base
            - if in front of character : hit him (and get reward)
        """
        if game.get_character_at(self.position + self.direction) == None:
            if self.direction == -1:
                if self.position[1] == 0:
                    self.enemy.get_hit(self.strength)

            elif self.direction == 1:
                if self.position[1] == game.nb_columns:
                    self.enemy.get_hit(self.strength)

        elif not game.get_character_at(self.position + self.direction) == None:
            if self.direction == -1:
                self.get_hit(self.strength)

            elif self.direction == 1:
                self.get_hit(self.strength)
            return self.player.money += reward

    def play_turn(self):
        """
        play one turn : move and attack
        """
        self.move()
        self.attack()

    def __str__(self):
        """
        return a string represent the current object
        """
        return f"perso ({self.price}$) || life : {self.life} || strength : [{self.strength}"


if __name__ == "__main__":
    print("Let's Play !!! ")
    # TODO
    zozo = Player("zozo", 30, 74)
    lolo = Player("lolo", 25, 10)
    game = Game(zozo, lolo)
    print(f"{zozo}\n{lolo}")
    print(game.current_player.__str__)
    print(game.oponent)
