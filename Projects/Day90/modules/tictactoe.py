import random
from typing import List


class TicTacToe:
    def __init__(self) -> None:
        """
        Initializes a new Tic Tac Toe game.

        Args:
        None

        Returns:
        None
        """
        self.board: List[str] = [" "] * 9
        self.current_player: str = "X"

    def draw_board(self) -> None:
        """
        Draws the Tic Tac Toe board.

        Args:
        None

        Returns:
        None
        """
        for i in range(0, 9, 3):
            row = self.board[i:i + 3]
            print("-------------")
            print("| {} | {} | {} |".format(*row))
        print("-------------")

    def make_move(self, position: int) -> bool:
        """
        Makes a move on the board.

        Args:
        position (int): The position where the player wants to make a move.

        Returns:
        bool: True if the move is made successfully, False otherwise.
        """
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        else:
            return False

    def switch_player(self) -> None:
        """
        Switches the current player.

        Args:
        None

        Returns:
        None
        """
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def is_winner(self, player: str) -> bool:
        """
        Checks if a player has won the game.

        Args:
        player (str): The player to check for a win.

        Returns:
        bool: True if the player has won, False otherwise.
        """
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                                (0, 4, 8), (2, 4, 6)]  # diagonals
        for comb in winning_combinations:
            if all(self.board[i] == player for i in comb):
                return True
        return False

    def is_board_full(self) -> bool:
        """
        Checks if the board is full.

        Args:
        None

        Returns:
        bool: True if the board is full, False otherwise.
        """
        return all(pos != ' ' for pos in self.board)

    def play(self) -> None:
        """
        Starts the Tic Tac Toe game.

        Args:
        None

        Returns:
        None
        """
        while True:
            if self.current_player == "X":
                position = int(input("Enter position (0-8): "))
            else:
                position = random.randint(0, 8)

            if self.make_move(position):
                self.draw_board()
                if self.is_winner(self.current_player):
                    print(self.current_player + " wins!")
                    return
                elif self.is_board_full():
                    print("It's a tie!")
                    return
                else:
                    self.switch_player()
            else:
                print("Position is already taken!")
