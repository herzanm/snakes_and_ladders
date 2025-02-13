import random

# Position of ladders and where they lead to
LADDERS = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    78: 98,
    87: 94
}

# Position of snakes and where they lead to
SNAKES = {
    16: 6,
    46: 25,
    49: 11,
    62: 19,
    64: 60,
    74: 53,
    89: 68,
    92: 88,
    95: 75,
    99:80
}

BOARD = LADDERS | SNAKES

# Players, position, moving
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps


class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.winner = None

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    @staticmethod
    def check_board(player):
        while player.position in BOARD:
            target = BOARD[player.position]
            direction = "našel žebřík" if target > player.position else "stoupl na hada"
            print(f"{player.name} {direction}! Posun na pole {target}.")
            player.position = target

    def play_turn(self, player):
        print(f"\n{player.name} je na tahu.")
        total_roll = 0

        while True:
            roll = self.roll_dice()
            total_roll += roll
            print(f"{player.name} hodil {roll}.")
            if roll != 6:
                break
            print(f"{player.name} hází znovu!")

        new_position = player.position + total_roll

        if new_position > 100:
            print(f"{player.name} nemůže překročit pole 100.")
            return

        player.position = new_position
        print(f"{player.name} se posunul na pole {player.position}.")

        self.check_board(player)

        for other_player in self.players:
            if other_player != player and other_player.position == player.position:
                print(f"{other_player.name} byl posunut zpět o jedno pole kvůli {player.name}.")
                other_player.position -= 1
                self.check_board(other_player)

        if player.position == 100:
            self.winner = player

    def play(self):
        print("Hra začíná!")
        while not self.winner:
            for player in self.players:
                self.play_turn(player)
                if self.winner:
                    break

        print(f"\n{self.winner.name} vyhrál hru!")

if __name__ == "__main__":
    names = input("Zadejte jména hráčů (oddělená čárkou): ").split(",")
    game = Game([name.strip() for name in names])
    game.play()