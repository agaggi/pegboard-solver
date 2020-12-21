import random
import copy

class Board:

    def __init__(self, size=4):

        '''Instances of this class are created with an inputted size that serves as the
        board dimensions.

        :param size: The dimension of the board (i.e. 4 => 4 x 4)
        '''

        self.size = size
        self.board = []


    def build_board(self):

        '''Builds a board of size n and appends a 0 at a random location within the
        board, serving as the start.
        '''

        # Creating the board with dimensions based off user input
        self.board = [['1' for _ in range(self.size)] for _ in range(self.size)]

        # Assigning a 0 to a random index
        self.board[random.randint(0, self.size - 1)]\
                  [random.randint(0, self.size - 1)] = '0'


    def print_board(self, board):

        '''Takes in a board state in the form of a 2D list and prints the state in a more
        readable format.

        :param board: The board state to be printed
        '''

        print()

        for i in range(self.size):

            print(' '.join(board[i]))


    def goal_message(self, nodes_explored, time):

        '''Returns a message indicating a solution has been found.

        :param nodes_explored: The number of nodes explored
        :param time: The time it took to find the solution
        :return: A message explaining what occurred
        '''

        return f'''
-- Goal state found! --

Unique nodes visited: {nodes_explored}
Execution Time: {time} seconds
'''


    def fail_message(self, nodes_explored, time):

        '''Returns a message indicating there was no solution.

        :param nodes_explored: The number of nodes explored
        :param time: The time it took to find the solution
        :return: A message explaining what occurred
        '''

        return f'''
-- There was no goal state. --
            
Unique nodes visited: {nodes_explored}
Execution Time: {time} seconds
'''


    def generate_moves(self, board):

        '''Takes in a board state and returns all possible moves.

        :param board: The board state to have its possible states generated
        :return: The possible states
        '''

        possible_moves = []

        for i in range(self.size):

            for j in range(self.size):

                if board[i][j] == '0':

                    row = i - 2

                    # If we are not not out of bounds and there's a possible jump down
                    if row >= 0 and board[i-1][j] == '1' and board[i-2][j] == '1':

                        board_copy = copy.deepcopy(board)

                        board_copy[i][j] = '1'
                        board_copy[i-1][j] = '0'
                        board_copy[i-2][j] = '0'

                        possible_moves.append(board_copy)

                    row = i + 2

                    # If we are not not out of bounds and there's a possible jump up
                    if row < self.size and board[i+1][j] == '1' and board[i+2][j] == '1':

                        board_copy = copy.deepcopy(board)

                        board_copy[i][j] = '1'
                        board_copy[i+1][j] = '0'
                        board_copy[i+2][j] = '0'

                        possible_moves.append(board_copy)

                    col = j - 2

                    # If we are not not out of bounds and there's a possible jump right
                    if col >= 0 and board[i][j-1] == '1' and board[i][j-2] == '1':

                        board_copy = copy.deepcopy(board)

                        board_copy[i][j] = '1'
                        board_copy[i][j-1] = '0'
                        board_copy[i][j-2] = '0'

                        possible_moves.append(board_copy)

                    col = j + 2

                    # If we are not not out of bounds and there's a possible jump left
                    if col < self.size and board[i][j+1] == '1' and board[i][j+2] == '1':

                        board_copy = copy.deepcopy(board)

                        board_copy[i][j] = '1'
                        board_copy[i][j+1] = '0'
                        board_copy[i][j+2] = '0'

                        possible_moves.append(board_copy)

        return possible_moves
