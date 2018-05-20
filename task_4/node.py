from board import Board


class Node:
    """
    Node for a tree node of tic-tac-toe.
    """
    def __init__(self):
        """
        Initialise...
        """
        self.board = Board()
        self.children = list()

        # This one is just for one method of a tree:
        self.score = None

    def get_state(self, symb="X"):
        """
        For faster access.
        :return: int
        """
        return self.board.get_state(symb)

    def set_field(self, list_of_lists):
        """
        For faster access.
        :param list_of_lists: list
        :return: NoneType
        """
        self.board.set_field(list_of_lists)

    def set_last_move(self, move_pos_tuple, move_symb_type):
        """
        For easier access.
        :param move_pos_tuple: tuple
        :param move_symb_type: bool
        :return: NoneType
        """
        self.board.set_last_move(move_pos_tuple, move_symb_type)

    def free_positions(self):
        """
        For easier access.
        :return: list
        """
        return self.board.free_positions()

    def set_board(self, board):
        """
        Change board of the node.
        :param board: Board
        :return: NoneType
        """
        self.board = board
