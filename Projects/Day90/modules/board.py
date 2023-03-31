class Board:
    """
    Represents the board game for Tic Tac Toe.

    Attributes:
        board_game (list): A list of strings representing the state of the board.

    Methods:
        display_board(): Displays the board game.
        update_board(position: int, marker: str) -> None: Updates the board with the specified marker at the given
        position.
        is_position_empty(position: int) -> bool: Returns True if the given position is empty, False otherwise.
        is_board_full() -> bool: Returns True if the board is full, False otherwise.
    """
    def __init__(self):
        self.board_game = [' '] * 9

    def display_board(self) -> None:
        """
        Displays the current state of the board.
        """
        board_rows = [self.board_game[i:i + 3] for i in range(0, 9, 3)]
        for row in board_rows:
            print(f" {' | '.join(row)} ")
            if row != board_rows[-1]:
                print('---+---+---')

    def update_board(self, position: int, marker: str) -> None:
        """
        Updates the board with the given marker at the specified position.

        Args:
            position (int): The position where the marker needs to be updated.
            marker (str): The marker to update the board with.

        Raises:
            ValueError: If the position is not within 1-9 range or if the position is already occupied.
        """
        if not 1 <= position <= 9:
            raise ValueError("Position should be between 1 and 9.")
        if not self.is_position_empty(position):
            raise ValueError("Position is already occupied.")
        self.board_game[position - 1] = marker

    def is_position_empty(self, position: int) -> bool:
        """
        Returns True if the given position is empty, False otherwise.

        Args:
            position (int): The position to check.

        Raises:
            ValueError: If the position is not within 1-9 range.

        Returns:
            bool: True if the given position is empty, False otherwise.
        """
        if not 1 <= position <= 9:
            raise ValueError("Position should be between 1 and 9.")
        return self.board_game[position - 1] == ' '

    def is_board_full(self) -> bool:
        """
        Returns True if the board is full, False otherwise.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        return ' ' not in self.board_game
