from board import Board
from collections import deque
from time import time

class Breadth:

    '''Class includes methods to build and generate solutions via Breadth First search.'''

    def __init__(self):

        self.b = Board()
        self.b.size = int(input('Enter board dimension (i.e. 4 for 4x4): '))
        self.deq = deque()
        self.numNodes = 0

        
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
        self.b.buildBoard(self.b.size)  

        # Printing the initial board for reference
        self.b.printBoard(self.b.board)

        # Calling the successor function to find a solution
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
        startTime = time()

        # While there are successors in the deque
        while self.deq:

            # Pop the first element and generate its successors
            state = self.deq.popleft()
            successors = self.b.movementCheck(state)
            
            for successor in successors:

                # Checks whether the successor state has been visited before
                if successor not in visited:

                    self.numNodes += 1

                    visited.append(successor)
                    self.deq.append(successor)

                    self.b.printBoard(successor)

                    # If the goal state is reached before the end of the deque
                    if self.goalState(successor):

                        endTime = time() - startTime
                        print(self.b.goalStatement(self.numNodes, endTime))
                        break
        
        # If a goal state was not found
        if not self.goalState(state):

            endTime = time() - startTime
            print(self.b.failStatement(self.numNodes, endTime))

                    
    def goalState(self, board):
        
        '''Checks whether a goal state has been reached.
        
        The board is scanned for the amount of pegs left. If there is 1 piece remaining,
        the goal state has been reached.
        '''

        sum = 0

        for i in range(self.b.size):

            sum += board[i].count('1')
        
        if sum == 1:

            return True

        else:

            return False