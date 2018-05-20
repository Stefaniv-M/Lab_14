class Board:
    """
    Class for representation of a gaming board for tic-tac-toe.
    """
    def __init__(self):
        """
        I will be using lists to store the field because I already know how to use
        2DArray. X is represented by False, O is represented by True, empty place
        is represented by None.
        """
        self.data = []
        for i in range(3):
            list_1 = []
            for j in range(3):
                list_1.append(None)
            self.data.append(list_1)

        self.last_move_symb = None
        self.last_move_pos = None

    def set_last_move(self, move_pos_tuple, move_symb_type):
        """
        Set last move of the board.
        :param move_pos_tuple: tuple
        :param move_symb_type: bool
        :return: NoneType
        """
        if type(move_symb_type) != bool:
            raise ValueError("In TickTackToe symbols can only be True or False.")
        if (not isinstance(move_pos_tuple, tuple)) or len(move_pos_tuple) != 2 or \
           move_pos_tuple[0] not in range(3) or move_pos_tuple[1] not in range(3):
            raise ValueError("Incorrect board position!")

        self.last_move_pos = move_pos_tuple
        self.last_move_symb = move_symb_type

    def set_field(self, list_of_lists):
        """
        Change field.
        :param list_of_lists: list
        :return: NoneType
        """
        for i in range(3):
            for j in range(3):
                self.data[i][j] = list_of_lists[i][j]

    def get_state(self, symb="X"):
        """
        Return 1 if player with symb won, return -1 if player with symb lost, return 0
        otherwise.
        :return: int
        """
        if symb not in ["X", "O"]:
            raise ValueError("In TickTackToe symbols can only be X or O.")

        def opposite(symb):
            """
            Helper function.
            :param symb: str
            :return: None
            """
            if symb == "X":
                return "O"
            elif symb == "O":
                return "X"
            elif symb:
                return False
            else:
                return True

        def to_bool(symb):
            """
            Helper function.
            :param symb: str
            :return: bool
            """
            if symb == "O":
                return True
            else:
                return False

        def to_symb(bul):
            """
            Helper function
            :param bul: bool
            :return: str
            """
            if bul:
                return "O"
            else:
                return "X"

        def check_line_win(board, symb):
            """
            Check if symb won on board.
            :param board: Board
            :param symb: str
            :return: bool
            """
            for line in board.data:
                if to_bool(symb) in line and (to_bool(opposite(symb)) not in line) and \
                        (None not in line):
                    return True
            return False

        def check_col_win(board, symb):
            """
            Check if symb won in column.
            :param board: Board
            :param symb: str
            :return: bool
            """
            for i in range(3):
                column = []
                # Creating column:
                for j in range(3):
                    column.append(board.data[j][i])
                # Checking:
                if to_bool(symb) in column and (to_bool(opposite(symb)) not in column) and \
                        (None not in column):
                    return True
            return False

        def check_cross_win(board, symb):
            """
            Check if player won by crossing the board.
            :param board: Board
            :param symb: str
            :return: bool
            """
            var_1 = [(0, 0), (1, 1), (2, 2)]
            var_2 = [(0, 2), (1, 1), (2, 0)]

            for var in (var_1, var_2):
                checker = 0
                for tupl in var:
                    if board.data[tupl[0]][tupl[1]] == to_bool(symb):
                        checker += 1
                if checker == 3:
                    return True
            return False

        # Checking if the player won:
        if check_line_win(self, symb) or check_col_win(self, symb) or check_cross_win(self, symb):
            return 1

        # Checking if the enemy won:
        symb = opposite(symb)
        if check_line_win(self, symb) or check_col_win(self, symb) or check_cross_win(self, symb):
            return -1

        # If nobody won:
        return 0

    def free_positions(self):
        """
        Return tuples with coordinates of positions with empty places.
        :return: list
        """
        result_list = []
        for i in range(3):
            for j in range(3):
                if self.data[i][j] is None:
                    result_list.append(tuple([i, j]))
        return result_list

    def print_board(self):
        """
        Print board.
        :return: NoneType
        """
        for line in self.data:
            for symb in line:
                if symb:
                    print("[O] ", end="")
                elif symb is False:
                    print("[X] ", end="")
                else:
                    print("[ ] ", end="")
            print()
        print("Last move: {}; position: {}.".format(self.last_move_symb, self.last_move_pos))
