AVAILABLE_CHARACTERS = {}
AVAILABLE_POTIONS = {}

class Character:
    base_price = 1
    base_life = 5
    base_strength = 1

    def __init__(self, player, position):
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
        x, y = self.position
        y += self.direction
        self.game.place_character(self, (x, y))

    def get_hit(self, damages):
        self.life -= damages
        reward = 0
        if self.life <= 0:
            self.player.team.remove(self)
            reward = self.price / 2
        return reward

    def attack(self):
        x, y = self.position
        base_oponent = self.game.nb_columns - 1 if self.direction == 1 else 0
        if y == base_oponent:
            self.enemy.get_hit(self.strength)
        else:
            character = self.game.get_character_at((x, y + self.direction))
            if character is None or character in self.player.team:
                return
            self.player.money += character.get_hit(self.strength)

    def play_turn(self):
        self.move()
        self.attack()

class Fighter(Character):
    base_price = 2
    base_life = 7
    base_strength = 3

    @property
    def design(self):
        return '+' if self.direction == 1 else '+'

    AVAILABLE_CHARACTERS["F"] = "Fighter - 2$ - ❤ 7 - Strenght : 3"

class Tank(Character):
    base_price = 5
    base_life = 10
    base_strength = 2

    def __init__(self, player, position):
        super().__init__(player, position)
        self.turn_to_move = False

    def move(self):
        if self.turn_to_move == True:
            super().move()
        self.turn_to_move = not self.turn_to_move

    @property
    def design(self):
        return '@' if self.direction == 1 else '@'

    AVAILABLE_CHARACTERS["T"] = "Tank - 5$ - ❤ 10 - Strenght : 2"

class Duck(Character):
    base_price = 8
    base_life = 3
    base_strength = 10

    @property
    def design(self):
        return '^' if self.direction == 1 else '^'

    AVAILABLE_CHARACTERS["D"] = "Duck - 8$ - ❤ 3 - Strenght : 10"

class Potion:
    base_price = 0
    base_damage = 0
    base_heal = 0

    def __init__(self, player):
        self.player = player
        self.price = self.base_price
        self.damage = self.base_damage
        self.heal = self.base_heal

class Heal(Potion):
    base_price = 5
    base_heal = 5

    def heal(self):
        if self.player.money <= self.base_price:
            self.player.life += self.base_heal

    AVAILABLE_POTIONS["H"] = "Heal : 5 life points - 5$"