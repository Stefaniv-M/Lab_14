from btnode import Node
from board import Board
import random
import copy


class Tree:
    """
    Tree for representation of binary search tree for tic-tac-toe.
    """
    def __init__(self, start_board=None):
        """
        Initialise tree by starting board.
        """
        # Root is a board without any step.
        self._root = Node()
        if start_board is None:
            self._root.set_board(Board())
        else:
            self._root.set_board(start_board)

    def finish(self):
        """
        Build search tree for given board.
        :return: NoneType
        """
        # Function for adding branches to given node.
        def add_branches(node):
            """
            Add two branches representing game moves to the node.
            Return 2 if process was successful. Return 1 if only one branch can be added.
            Return 0 if node board is full.
            :param node: Node
            :return: int
            """
            if not isinstance(node, Node):
                raise ValueError("You can only add branches to Node!")

            # Helper function:
            def new_node(node, pos):
                """
                Helper function for creating a new node in which player moved to pos.
                :param node: Node
                :param pos: tuple
                :return: Node
                """
                new_node = Node()
                list_of_lists = copy.deepcopy(node.board.data)
                new_node.set_field(list_of_lists)
                new_node.set_last_move(pos, not node.board.last_move_symb)
                new_node.board.data[pos[0]][pos[1]] = not node.board.last_move_symb
                return new_node

            # If there are no free positions in a node:
            if not node.free_positions():
                return 0

            # Other variants:
            if len(node.free_positions()) == 1:
                tupl = node.free_positions()[0]
                # Creating a new node and passing down there information from previous one:
                node.left = new_node(node, tupl)
                return 1

            else:
                positions = node.free_positions()

                # Choosing two random positions:
                pos1 = random.choice(positions)
                positions.pop(positions.index(pos1))
                pos2 = random.choice(positions)

                # Creating new nodes representing positions:
                node.left = new_node(node, pos1)
                node.right = new_node(node, pos2)

                return 2

        # List of nodes, for which branches are yet to be added:
        node_list = [self._root]

        # Adding branches:
        while node_list:
            new_node_list = []

            for node in node_list:
                check_val = add_branches(node)

                # Adding nodes to new_node_list
                if check_val == 2:
                    new_node_list.append(node.left)
                    new_node_list.append(node.right)
                elif check_val == 1:
                    new_node_list.append(node.left)

            # Changing node_list:
            node_list = new_node_list

    def print_tree(self):
        """
        Print some representation of a tree.
        :return: NoneType
        """
        node_list = [self._root]

        while node_list:
            new_node_list = []
            for node in node_list:
                node.board.print_board()
                print("________________________________________")
                if node.left is not None:
                    new_node_list.append(node.left)
                if node.right is not None:
                    new_node_list.append(node.right)
            print("_______________________________________\n"
                  "_______________________________________")
            node_list = new_node_list

    def best_board(self):
        """
        Return best move for the tree by counting scores for two children of a root.
        :return: Board
        """
        def find_score(node):
            """
            Find score of a node.
            :param node: Node or NoneType
            :return: int
            """
            if node is None:
                return 0
            else:
                left_score = find_score(node.left)
                right_score = find_score(node.right)
                node_score = node.get_state()
                return left_score + right_score + node_score

        if self._root.right is None and self._root.left is None:
            raise ValueError("Best_board function problem: no variants are available!")
        elif self._root.right is None:
            return self._root.left.board
        else:
            if find_score(self._root.left) > find_score(self._root.right):
                return self._root.left.board
            else:
                return self._root.right.board
