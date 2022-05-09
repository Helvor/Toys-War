class Game:

    def __init__(self, player0, player1, nb_lines=6, nb_columns=15):
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
        actual_character = None
        for character in self.all_characters:
            if character.position == position:
                actual_character = character
        return actual_character

    def place_character(self, character, position):
        if (0, 0) <= position < (self.nb_lines, self.nb_columns):
            if self.get_character_at((position[0], position[1])) == None:
                character.position = position
                return True
            else:
                return False

    def draw(self):
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
        self.draw()
        self.current_player.new_character()
        for character in self.current_player.team + self.oponent.team:
            character.play_turn()
        self.current_player.money += 1

    def play(self):
        while self.current_player.is_alive and self.oponent.is_alive:
            self.play_turn()
            self.player_turn = 1 - self.player_turn
