import collections
import time

from board import Board

START = time.time()

class Greedy:

    def __init__(self):

        '''Class includes methods to build and generate solutions via Greedy Best First
        search.'''

        self.b = Board()
        self.b.size = int(input('Enter board dimension (i.e. 4 for 4x4): '))

        self.deq = collections.deque()
        self.visited = []

        self.nodes_explored = 0
        self.solved = False


    def generate(self):

        '''User input for board size is validated whether it lies within bounds, 4x4 to
        10x10; if not, the user is reprompted. After a legal input, a board instance is
        generated with the inputted size and the successor function is called to look for
        a solution.
        '''

        while self.b.size < 4 or self.b.size > 10:

            print('\n-- Enter a dimension between 4 to 10 --\n')
            self.b.size = int(input('Enter board dimension (i.e. 4 for 4x4): '))

        # Creating a board instance with the inputted size
        self.b = Board(self.b.size)
        self.b.build_board()

        # Printing the initial board for reference
        self.b.print_board(self.b.board)

        # Calling the successor with the initial board as the starting point
        self.successor(self.b.board)

        # If there was no goal state found
        if not self.solved:

            end_time = time.time() - START
            print(self.b.fail_message(self.nodes_explored, end_time))


    def successor(self, board):

        '''Determines all possible solutions from a given state.

        The successor function will run as long as there are successors in the deque.
        Newer successors with more desirable heuristic values are appended at the
        beginning of the deque and are computed first via recursion. Whether a board
        state has been visited before is checked and, if it has not been visited, the
        state will be appended to a list of unique board states.

        If the goal state is reached before the loop ends, the loop will break and output
        the result. Otherwise, if there is no solution found, the loop will continue to
        run until there are no more successors.

        :param board: The board state to have its successors generated
        '''

        # Serves as appending the initial board into the deque.
        # We do not want to run this recursively and append each board state twice.
        if self.nodes_explored == 0:

            self.deq.append(board)

        # While there are successors in the queue
        while self.deq:

            # Pop the last element and generate its successors
            state = self.deq.pop()
            successors = self.b.generate_moves(state)

            # Using the heuristic function to pick the more promising state
            successors = self.heuristic(successors)

            for successor in successors:

                # Checks whether the successor state has been visited before
                if successor not in self.visited:

                    self.nodes_explored += 1

                    self.visited.append(successor)
                    self.deq.append(successor)

                    self.b.print_board(successor)

                    # If the goal state is reached before the end of the deque
                    if self.goal_state(successor):

                        end_time = time.time() - START
                        exit(self.b.goal_message(self.nodes_explored, end_time))

                    # Ensures the current successor's successors will be generated next.
                    # Once a given branch has ended, the next is then recursively called.
                    self.successor(successor)


    def heuristic(self, successors):

        '''Implements Manhatten distance in order to determine the most promising state
        in a list of successors.

        The Manhatten distance of each successor state is determined by the sum of
        each pegs' distance from the center of the board. After Manhatten distance is
        calculated, the successor states are sorted by least distance.
        '''

        # Obtaining the center coordinate of the board.
        # -- If odd (i.e. 5x5), the center is exact
        # -- If even (i.e. 4x4), we try to get as close to the "center" as possible
        x_center = int((self.b.size - 1) / 2)
        y_center = int((self.b.size - 1) / 2)

        new_list = []

        for successor in successors:

            distance = 0

            for curr_x in range(self.b.size):

                for curr_y in range(self.b.size):

                    if successor[curr_x][curr_y] == '1':

                        # Formula for Manhatten distance
                        distance += abs(curr_x - x_center) + abs(curr_y - y_center)

            new_list.append([successor, distance])

        # Sort list by second element (i.e. distance)
        new_list.sort(reverse=False, key=lambda successor: successor[1])
        sorted_successors = [new_list[i][0] for i in range(len(new_list))]

        return sorted_successors


    def goal_state(self, board):

        '''Checks whether a goal state has been reached.

        The board is scanned for the amount of pegs left. If there is 1 piece remaining,
        the goal state has been reached.
        '''

        num_pegs = 0

        for i in range(self.b.size):

            num_pegs += board[i].count('1')

        if num_pegs == 1:

            return True

        return False
