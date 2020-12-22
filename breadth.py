import collections
import time

from board import Board

class Breadth:

    def __init__(self):

        '''Class includes methods to build and generate solutions via Breadth First
        search.
        '''

        self.b = Board()
        self.b.size = int(input('Enter board dimension (i.e. 4 for 4x4): '))

        self.deq = collections.deque()
        self.nodes_explored = 0


    def generate(self):

        '''User input for board size is validated whether it lies within bounds, 4x4 to
        8x8; if not, the user is reprompted. After a legal input, a board instance is
        generated with the inputted size and the successor function is called to look for
        a solution.
        '''

        while not 4 <= self.b.size <= 8:

            print('\n-- Enter a dimension between 4 to 8 --\n')
            self.b.size = int(input('Enter board dimension (i.e. 4 for 4x4): '))

        # Creating a board instance with the inputted size
        self.b = Board(self.b.size)
        self.b.build_board()

        # Printing the initial board for reference
        self.b.print_board(self.b.board)

        # Calling the successor with the initial board as the starting point
        self.successor()


    def successor(self):

        '''Determines all possible solutions from a given state.

        The successor function will run as long as there are successors in the deque.
        Newer successors are appended at the end of the deque. Whether a board state has
        been visited before is checked and, if it has not been visited, the state will be
        appended to a list of unique board states.

        If the goal state is reached before the loop ends, the loop will break and output
        the result. Otherwise, if there is no solution found, the loop will continue to
        run until there are no more successors.
        '''

        # Appending the initial board to the deque
        self.deq.append(self.b.board)

        visited = []
        start_time = time.time()

        # While there are successors in the deque
        while self.deq:

            # Pop the first element and generate its successors
            state = self.deq.popleft()
            successors = self.b.generate_moves(state)

            for successor in successors:

                # Checks whether the successor state has been visited before
                if successor not in visited:

                    self.nodes_explored += 1

                    visited.append(successor)
                    self.deq.append(successor)

                    self.b.print_board(successor)

                    # If the goal state is reached before the end of the deque
                    if self.goal_state(successor):

                        end_time = time.time() - start_time
                        exit(self.b.goal_message(self.nodes_explored, end_time))

        # If a goal state was not found
        if not self.goal_state(state):

            end_time = time.time() - start_time
            print(self.b.fail_message(self.nodes_explored, end_time))


    def goal_state(self, board):

        '''Checks whether a goal state has been reached.

        The board is scanned for the amount of pegs left. If there is 1 piece remaining,
        the goal state has been reached.

        :param board: The board state to be checked
        :return: Whether a solution has been found or not
        '''

        num_pegs = 0

        for i in range(self.b.size):

            num_pegs += board[i].count('1')

        if num_pegs == 1:

            return True

        return False
