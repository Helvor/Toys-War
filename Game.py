from squelette import Player

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
