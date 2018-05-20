from node import Node
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
            Add branches representing game moves to the node.
            Return True if some branches were added. Return False if no branches were added.
            :param node: Node
            :return: bool
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
                return False
            # Otherwise:
            else:
                for pos_tuple in node.free_positions():
                    # Adding a new move:
                    node.children.append(new_node(node, pos_tuple))
                return True

        # List of nodes, for which branches are yet to be added:
        node_list = [self._root]

        # Adding branches:
        while node_list:
            new_node_list = []

            for node in node_list:
                check_val = add_branches(node)

                # Adding nodes to new_node_list
                for node_1 in node.children:
                    new_node_list.append(node_1)

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
                for node_1 in node.children:
                    new_node_list.append(node_1)
            print("_______________________________________\n"
                  "_______________________________________")
            node_list = new_node_list

    def best_board(self):
        """
        Return best move for the tree by counting scores for two children of a root.
        :return: Board
        """
        if not self._root.children:
            raise ValueError("Best_board function problem: no variants are available!")
        else:
            list_of_nodes = copy.deepcopy(self._root.children)
            list_of_nodes.sort(key=lambda node: node.get_state())
            for node in list_of_nodes:
                if node.get_state(symb="O") == 1:
                    return node.board
            # Looking closer for winning chance and losing chance:
            while True:
                # Choosing a winning position if it is a win for granted:
                if 1 in [nod.get_state("O") for nod in list_of_nodes]:
                    # Finding index of winning position:
                    index = [nod.get_state("O") for nod in list_of_nodes].index(1)
                    return list_of_nodes[index]
                # Eliminating loosing positions:
                elif len(list_of_nodes) > 1 and (list_of_nodes[-1].board.get_state("O") == -1 or
                   -1 in [nod.get_state("O") for nod in list_of_nodes[-1].children]):
                    list_of_nodes.pop()
                # Otherwise:
                else:
                    return list_of_nodes[-1].board
    @staticmethod
    def find_score(node):
        """
        Find score of a node.
        :param node: Node or NoneType
        :return: int
        """
        if node is None:
            return 0
        else:
            score = 0
            for child in node.children:
                score += Tree.find_score(child)
            return score
