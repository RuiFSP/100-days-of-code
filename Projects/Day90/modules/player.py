class Player:
    """
    A class representing a player in the tic-tac-toe game.

    Attributes:
        name (str): The name of the player.
        marker (str): The marker (X or O) used by the player.

    Methods:
        get_move() -> int:
            Prompts the player to enter their move (1-9) and returns the integer value of the move.
    """

    def __init__(self, name: str, marker: str):
        """
        Initializes a new instance of the Player class with the specified name and marker.

        Args:
            name (str): The name of the player.
            marker (str): The marker (X or O) used by the player.
        """
        self.name = name
        self.marker = marker

    def get_move(self) -> int:
        """
        Prompts the player to enter their move (1-9) and returns the integer value of the move.

        Returns:
            int: The integer value of the player's move.
        """
        while True:
            try:
                move = int(input(f'{self.name}, enter your move (1-9): '))
                if 1 <= move <= 9:
                    return move
                else:
                    print('Move must be between 1 and 9. Try again.')
            except ValueError:
                print('Invalid input. Try again.')

