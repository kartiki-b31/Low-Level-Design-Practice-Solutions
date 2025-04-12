import random
import threading

# Creating the class for Snake
class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    # Creating the methods for star and end points
    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

# Creating the class for Ladder
class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    # Crreating the methods for start and end points
    def get_start(self):
        return self.start

    def get_end(self):
        return self.end
    
# Creating the class for Rolling the Dice
class Dice:
    MIN_VALUE = 1
    MAX_VALUE = 6
        
    # Creating the method for rolling the dice
    def roll(self):
        return random.randint(Dice.MIN_VALUE, Dice.MAX_VALUE)

# Creating the class for Board
class Board:
    BOARD_SIZE = 100

    def __init__(self):
        self.snakes = []
        self.ladders = []
        self._initialize_snake_and_ladder()

    def _initialize_snake_and_ladder(self):
        # Initialize snakes
        self.snakes.append(Snake(16, 6))
        self.snakes.append(Snake(48, 26))
        self.snakes.append(Snake(64, 60))
        self.snakes.append(Snake(93, 73))

        # Initialize ladders
        self.ladders.append(Ladder(1, 38))
        self.ladders.append(Ladder(4, 14))
        self.ladders.append(Ladder(9, 31))
        self.ladders.append(Ladder(21, 42))
        self.ladders.append(Ladder(28, 84))
        self.ladders.append(Ladder(51, 67))
        self.ladders.append(Ladder(80, 99))
    
    # Creating the method for getting the board size
    def get_board_size(self):
        return Board.BOARD_SIZE

    # Creating the method for getting the new position after snake or ladder
    def get_new_position(self, position):
        for snake in self.snakes:
            if snake.get_start() == position:
                return snake.get_end()
        
        for ladder in self.ladders:
            if ladder.get_start() == position:
                return ladder.get_end()

        return position
    
# Creating the player class
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    # Creating the method for get_name
    def get_name(self):
        return self.name
    
    # Creating the method for get_position
    def get_position(self):
        return self.position

    # Creating the method for set_position
    def set_position(self, position):
        self.position = position
    
# Creating the class for snake_and_ladder
class Snake_And_Ladder:
    def __init__(self, player_names):
        self.board = Board()
        self.dice = Dice()
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0

    # Creating the method for play
    def play(self):
        while not self._game_over():
            current_player = self.players[self.current_player_index]
            dice_roll = self.dice.roll()
            new_position = current_player.get_position() + dice_roll

            if new_position <= self.board.get_board_size():
                current_player.set_position(self.board.get_new_position(new_position))
                print(f"{current_player.get_name()} rolled a {dice_roll} and moved to position {current_player.get_position()}")
            if new_position == self.board.get_board_size():
                print(f"{current_player.get_name()} is the winner !!!!...")
                break

            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def _game_over(self):
        for player in self.players:
            if player.get_position() == self.board.get_board_size():
                return True
        return False

# Creating the class for GameManager
class GameManager:
    _instance = None
    # _lock = threading.Lock()
    
    # Initialising the class
    def __init__(self):
        self.games = []

    @staticmethod
    def get_instance():
        if not GameManager._instance:
            GameManager._instance = GameManager()
        return GameManager._instance

    # Creating method to start a new game
    def start_new_game(self, player_names):
        game = Snake_And_Ladder(player_names)
        self.games.append(game)
        game.play()

    
# Creating the main function
if __name__ == "__main__":

    game_manager = GameManager.get_instance()

    # Starting the new game
    players_list = ["Arun", "Erick", "David"]
    game_manager.start_new_game(players_list)