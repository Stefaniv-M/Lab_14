# Main module for the tic-tac-toe game:
from btree import Tree
from board import Board
from btnode import Node


def main():
    """
    Main function for the game.
    :return: NoneType
    """
    print("Game start!")
    empty_board = Board()
    empty_board.print_board()
    print("_" * 120)

    print("Player goes first!")

    # How game:
    board = empty_board
    while True:
        board = game(board)
        state = board.get_state()
        if state == 1:
            print("Player won!")
            return None
        elif state == -1:
            print("Robot won!")
            return None


def game(board):
    """
    Start two moves - first one of a player, second one of a computer. Return Board
    representation of result.
    :param board: Board
    :return: Board
    """
    # I know how to use exceptions, but here it would be too hard, because I have to continue game.
    def get_pos(text):
        """
        Get number from one to three from player.
        :param text: str
        :return: int
        """
        i = input(text)
        if i in ['1', '2', '0']:
            return int(i)
        else:
            print("Sorry, you had to enter a number from 0 to 2! Please, try again!")
            return get_pos(text)

    def get_input(board):
        """
        Get position from player.
        :param board: Board
        :return: tuple
        """
        # Getting player input:
        col = get_pos("Player, please, enter column number (from 0 to 2): ")
        row = get_pos("Player, please, enter row number (from 0 to 2): ")

        # Checking input:
        if tuple([row, col]) not in board.free_positions():
            print("Sorry, but this position is not free! Please, try again!")
            return get_input(board)

        return tuple([row, col])

    # First move is made by a player.
    tupl = get_input(board)

    row = tupl[0]
    col = tupl[1]

    # Make a new board:
    new_board = Board()

    # Make a move on a new board:
    field = board.data[:]
    field[row][col] = False
    new_board.set_field(field)
    new_board.set_last_move(tupl, False)

    # Check if game is finished and if it is, return new board.
    if new_board.get_state() == 1 or not new_board.free_positions():
        return new_board

    # Print new version of a board on the screen:
    new_board.print_board()
    print("_" * 120)

    # Now it is time for a robot to choose its path.
    # Building a binary search tree:
    tree = Tree(new_board)
    tree.finish()
    final_board = tree.best_board()

    print("Robot made its choice!")
    final_board.print_board()
    print("_" * 120)

    return final_board


main()
