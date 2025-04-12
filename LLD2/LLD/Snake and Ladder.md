
## Requirements

1. The game should be played on a board with numbered cells, typically with 100 cells.
2. The board should have a predefined set of snakes and ladders, connecting certain cells.
3. The game should support multiple players, each represented by a unique game piece.
4. Players should take turns rolling a dice to determine the number of cells to move forward.
5. If a player lands on a cell with the head of a snake, they should slide down to the cell with the tail of the snake.
6. If a player lands on a cell with the base of a ladder, they should climb up to the cell at the top of the ladder.
7. The game should continue until one of the players reaches the final cell on the board.
8. The game should handle multiple game sessions concurrently, allowing different groups of players to play independently.

## Classes, Interfaces and Enumerations

1. The **Board** class represents the game board with a fixed size (e.g., 100 cells). It contains the positions of snakes and ladders and provides methods to initialize them and retrieve the new position after encountering a snake or ladder.
2. The **Player** class represents a player in the game, with properties such as name and current position on the board.
3. The **Snake** class represents a snake on the board, with properties for the start and end positions.
4. The **Ladder** class represents a ladder on the board, with properties for the start and end positions.
5. The **Dice** class represents a dice used in the game, with a method to roll the dice and return a random value between 1 and 6.
6. The **SnakeAndLadderGame** class represents a single game session. It initializes the game with a board, a list of players, and a dice. The play method handles the game loop, where players take turns rolling the dice and moving their positions on the board. It checks for snakes and ladders and updates the player's position accordingly. The game continues until a player reaches the final position on the board.
7. The **GameManager** class is a singleton that manages multiple game sessions. It maintains a list of active games and provides a method to start a new game with a list of player names. Each game is started in a separate thread to allow concurrent game sessions.
8. The **SnakeAndLadderDemo** class demonstrates the usage of the game by creating an instance of the GameManager and starting two separate game sessions with different sets of players.


---

## **1. Why These Classes Were Chosen?**

To implement a structured and scalable **Snake and Ladder game**, the system is broken down into different classes, each responsible for a **specific function**. This makes the code easier to understand, maintain, and extend in the future.

- **`Snake` and `Ladder` Classes** → Represent game elements that modify player movement.
- **`Board` Class** → Manages the board, snakes, ladders, and player movement.
- **`Dice` Class** → Represents a six-sided dice for rolling random values.
- **`Player` Class** → Holds individual player information and position.
- **`SnakeAndLadderGame` Class** → Runs the core gameplay loop, handling player turns and movement.
- **`GameManager` Class (Singleton)** → Manages multiple game sessions using threading.

---

## **2. Understanding Each Class in Detail**

### **2.1. `Snake` and `Ladder` Classes (Game Elements)**

- These classes define **snakes** and **ladders** on the board.
- **Snakes:** If a player lands on the snake’s head, they move to its tail.
- **Ladders:** If a player lands at the base of a ladder, they climb to the top.
- Each class has `start` (entry point) and `end` (exit point) positions.

> 📝 **Why Not Use One Class for Both?**  
> While both have start and end points, their **game mechanics differ**—snakes move players **down**, ladders move them **up**. Keeping them separate improves readability and future extensions.

---

### **2.2. `Board` Class (Manages the Game Board)**

- The **`Board`** class creates a **100-cell game board**.
- It **stores snakes and ladders** as lists and initializes them in `_initialize_snakes_and_ladders()`.
- The **`get_new_position_after_snake_or_ladder()`** method updates the player’s position if they land on a snake or ladder.

> 📝 **Why Have a Separate `Board` Class?**  
> This allows us to **decouple** board logic from the game flow. If we want a **custom board size**, we can easily modify it without changing the game logic.

---

### **2.3. `Dice` Class (Rolling Mechanism)**

- Represents a **standard 6-sided dice** used in the game.
- Uses `random.randint(1, 6)` to simulate rolling.

> 📝 **Why Have a Separate `Dice` Class?**  
> Keeping dice logic separate allows us to **extend it** easily. For example, in a different game mode, we could add a **special dice** (e.g., allowing double rolls).

---

### **2.4. `Player` Class (Represents a Game Participant)**

- Each player has a **name** and **current position** on the board.
- The `set_position()` method updates their position after dice rolls.

> 📝 **Why Store Players as Objects?**  
> This makes it easier to track **multiple players** with unique attributes. If we later add **avatars, scores, or power-ups**, they can be stored in the player object.

---

### **2.5. `SnakeAndLadderGame` Class (Core Game Engine)**

This class handles:

1. **Initializing the board and dice.**
2. **Managing multiple players.**
3. **Running the game loop** (players take turns rolling the dice).
4. **Checking for win conditions.**

#### **How the Gameplay Works:**

- Players take turns rolling the dice.
- Their position is updated using `board.get_new_position_after_snake_or_ladder()`.
- The game ends when **any player reaches cell 100**.

> 📝 **Why Does `SnakeAndLadderGame` Have a Loop?**  
> The game **doesn't stop** after one roll—it **continues until a player wins**. The loop ensures each player keeps playing in turn.

---

### **2.6. `GameManager` Class (Handles Multiple Games)**

This is a **Singleton Class** that manages multiple game sessions.  
**Singleton Pattern** ensures only **one instance** of `GameManager` exists in memory.

#### **Key Responsibilities:**

- Maintains a list of **active games**.
- Starts new games using **separate threads** (`threading.Thread(target=game.play).start()`).

> 📝 **Why Use `threading.Thread()`?**
> 
> - Allows multiple games to run **simultaneously**.
> - Players in **Game 1** don’t have to wait for **Game 2** to finish.
> - This makes the system **scalable** (e.g., handling 100+ games at once).

---

## **3. Object Creation & Initialization**

### **Where Are Objects Created?**

- `GameManager` is initialized **once** using `get_instance()`.
- `SnakeAndLadderGame` is created inside `GameManager.start_new_game()`.
- `Board`, `Dice`, and `Player` objects are created inside `SnakeAndLadderGame.__init__()`.
- `Snake` and `Ladder` objects are created inside `Board._initialize_snakes_and_ladders()`.

### **Where Are Objects Used?**

- The **board** object keeps track of snakes, ladders, and movement logic.
- The **dice** object is rolled each turn to generate a random move.
- The **player** objects are stored in a list (`self.players`) and updated each turn.

---

## **4. Running the Game**

When the script runs:

1. A **`GameManager`** instance is created (`game_manager = GameManager.get_instance()`).
2. A **new game** starts with **3 players** (`game_manager.start_new_game(players1)`).
3. The game runs in a **separate thread** (`threading.Thread(target=game.play()).start()`).
4. Players take turns rolling dice and moving.
5. The game ends when **one player reaches 100**.

---

## **5. Key Takeaways & Design Decisions**

✔ **Why Use Classes?**  
Each class has a **clear responsibility**—making the system modular, scalable, and easy to modify.

✔ **Why Use Threads?**  
Multiple games can run **simultaneously** without blocking each other.

✔ **Why Singleton for `GameManager`?**  
Ensures that there is **one central game manager**, preventing duplicate instances from interfering.

✔ **Why Separate `Board`, `Dice`, `Player` Classes?**  
Encapsulation improves **code organization** and **maintainability**.

✔ **Why Store Players as Objects?**  
Allows adding **player-specific features** later (e.g., avatars, rankings).


```
import random

import threading

  

# Snake Class

class Snake:

    def __init__(self, start, end):

        self.start = start

        self.end = end

  

    def get_start(self):

        return self.start

  

    def get_end(self):

        return self.end

  
  

# Ladder Class

class Ladder:

    def __init__(self, start, end):

        self.start = start

        self.end = end

  

    def get_start(self):

        return self.start

  

    def get_end(self):

        return self.end

  
  

# Board Class

class Board:

    BOARD_SIZE = 100

  

    def __init__(self):

        self.snakes = []

        self.ladders = []

        self._initialize_snakes_and_ladders()

  

    def _initialize_snakes_and_ladders(self):

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

  

    def get_board_size(self):

        return Board.BOARD_SIZE

  

    def get_new_position_after_snake_or_ladder(self, position):

        for snake in self.snakes:

            if snake.get_start() == position:

                return snake.get_end()

  

        for ladder in self.ladders:

            if ladder.get_start() == position:

                return ladder.get_end()

  

        return position

  
  

# Dice Class

class Dice:

    MIN_VALUE = 1

    MAX_VALUE = 6

  

    def roll(self):

        return random.randint(Dice.MIN_VALUE, Dice.MAX_VALUE)

  
  

# Player Class

class Player:

    def __init__(self, name):

        self.name = name

        self.position = 0

  

    def get_name(self):

        return self.name

  

    def get_position(self):

        return self.position

  

    def set_position(self, position):

        self.position = position

  
  

# Snake and Ladder Game Class

class SnakeAndLadderGame:

    def __init__(self, player_names):

        self.board = Board()

        self.dice = Dice()

        self.players = [Player(name) for name in player_names]

        self.current_player_index = 0

  

    def play(self):

        while not self._is_game_over():

            current_player = self.players[self.current_player_index]

            dice_roll = self.dice.roll()

            new_position = current_player.get_position() + dice_roll

  

            if new_position <= self.board.get_board_size():

                current_player.set_position(self.board.get_new_position_after_snake_or_ladder(new_position))

                print(f"{current_player.get_name()} rolled a {dice_roll} and moved to position {current_player.get_position()}")

  

            if current_player.get_position() == self.board.get_board_size():

                print(f"{current_player.get_name()} wins!")

                break

  

            self.current_player_index = (self.current_player_index + 1) % len(self.players)

  

    def _is_game_over(self):

        for player in self.players:

            if player.get_position() == self.board.get_board_size():

                return True

        return False

  
  

# Game Manager (Singleton)

class GameManager:

    _instance = None

    _lock = threading.Lock()

  

    def __init__(self):

        self.games = []

  

    @staticmethod

    def get_instance():

        if not GameManager._instance:

            with GameManager._lock:

                if not GameManager._instance:

                    GameManager._instance = GameManager()

        return GameManager._instance

  

    def start_new_game(self, player_names):

        game = SnakeAndLadderGame(player_names)

        self.games.append(game)

        threading.Thread(target=game.play).start()

  
  

# Demo Execution

if __name__ == "__main__":

    game_manager = GameManager.get_instance()

  

    # Start game 1

    players1 = ["Player 1", "Player 2", "Player 3"]

    game_manager.start_new_game(players1)

  

    # # Start game 2

    # players2 = ["Player 4", "Player 5"]

    # game_manager.start_new_game(players2)
```