from Projects.Day90.modules.tictactoe import TicTacToe

def main() -> None:
    """
    The main function that runs the TicTacToe game.
    """
    game = TicTacToe()
    game.draw_board()
    game.play()


if __name__ == "__main__":
    main()
