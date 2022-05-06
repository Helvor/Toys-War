available_characters = {}

class Character:
    base_price = 1
    base_life = 5
    base_strength = 1
    name = "Character"

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
        if ok:
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
        return self.game.players[1 if self.direction == 1 else 0]

    @property
    def design(self):
        return '>' if self.direction == 1 else '<'

    def move(self):
        """
        the character move one step front
        """
        x, y = self.position
        y += self.direction
        self.game.place_character(self, (x, y))

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
        x, y = self.position
        base_oponent = self.game.nb_columns - 1 if self.direction == 1 else 0

        if y == base_oponent:
            self.enemy.get_hit(self.strength)
        else:
            character = self.game.get_character_at((x, y + self.direction))

            if character is None:
                return

            self.player.money += character.get_hit(self.strength)

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
        return f"{self.base_price}$ - Strenght : {self.base_strength} - Life : {self.base_life}"


class Fighter(Character):
    base_price = 2
    base_life = 7
    base_strength = 3

    def __str__(self):
        return f"{self.name[:1]} - {self.name} : {self.base_price}$ - Strenght : {self.base_strength} - Life : {self.base_life}"

    @property
    def design(self):
        return '+' if self.direction == 1 else '+'

    available_characters["F"] = "Fighter - 2$ - ❤ 7 - Strenght : 3"


class Tank(Character):
    base_price = 5
    base_life = 10
    base_strength = 2

    def __init__(self, player, position):
        super().__init__(player, position)

        self.turn_to_move = False

    def __str__(self):
        return f"{self.name[:1]} - {self.name} : {self.base_price}$ - Strenght : {self.base_strength} - Life : {self.base_life}"

    def move(self):
        if self.turn_to_move == True:
            super().move()
        if self.turn_to_move:
            self.turn_to_move = False
        elif not self.turn_to_move:
            self.turn_to_move = True

    @property
    def design(self):
        return '@' if self.direction == 1 else '@'

    available_characters["T"] = "Tank - 5$ - ❤ 10 - Strenght : 2"


class Duck(Character):
    base_price = 8
    base_life = 3
    base_strength = 10

    def __str__(self):
        return f"{self.name[:1]} - {self.name} : {self.base_price}$ - Strenght : {self.base_strength} - Life : {self.base_life}"

    @property
    def design(self):
        return '^' if self.direction == 1 else '^'

    available_characters["D"] = "Duck - 8$ - ❤ 3 - Strenght : 10"
