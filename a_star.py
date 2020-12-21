from board import Board
from collections import deque
from time import time

class A_Star:

    '''Class includes methods to build and generate solutions via A* search.'''

    def __init__(self):

        self.b = Board()
        self.b.size = int(input('Enter board dimension (i.e. 4 for 4x4): '))

        self.deq = deque()
        self.visited = []

        self.numNodes = 0
        self.startTime = 0
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
        self.b.buildBoard(self.b.size)  

        # Printing the initial board for reference
        self.b.printBoard(self.b.board)

        # Calling the successor with the initial board as the starting point
        self.successor(self.b.board)

        # If there was no goal state found
        if not self.solved:

            endTime = time() - self.startTime
            print(self.b.failStatement(self.numNodes, endTime))

        
    def successor(self, board):

        '''Determines all possible solutions from a given state.
        
        The successor function will run as long as there are successors in the deque.
        Newer successors with more desirable heuristic values and path costs are appended
        at the beginning of the deque and are computed first via recursion. Whether a
        board state has been visited before is checked and, if it has not been visited,
        the state will be appended to a list of unique board states. 
        
        If the goal state is reached before the loop ends, the loop will break and output
        the result. Otherwise, if there is no solution found, the loop will continue to
        run until there are no more successors.
        '''

        # Serves as appending the initial board into the deque.
        # We do not want to run this recursively and append each board state twice.
        if self.numNodes == 0:

            self.startTime = time()
            self.deq.append(board)

        # While there are successors in the queue
        while self.deq:

            # Pop the last element and generate its successors
            state = self.deq.pop()
            successors = self.b.movementCheck(state)

            # Using the heuristic function to pick the more promising state
            successors = self.heuristic(successors)
            
            for successor in successors:

                # Checks whether the successor state has been visited before
                if successor not in self.visited:

                    self.numNodes += 1

                    self.visited.append(successor)
                    self.deq.append(successor)

                    self.b.printBoard(successor)

                    # If the goal state is reached before the end of the deque
                    if self.goalState(successor):

                        endTime = time() - self.startTime
                        exit(self.b.goalStatement(self.numNodes, endTime))
                    
                    # Ensures the current successor's successors will be generated next.
                    # Once a given branch has ended, the next is then recursively called.
                    self.successor(successor)

    
    def heuristic(self, successors):
        
        '''Implements Manhatten distance in order to determine the most promising state
        in a list of successors.

        This function takes in a list of successors as an arguement and appends its
        contents to a dictionary. While doing so, the Manhatten distance of each state is
        determined by the sum of each pegs' distance from the center of the board; this
        is also stored in the dictionary. Path cost will be added as well.
        
        After the calculations, we are left with a list of Manhatten distance values and
        the successor states as our dictionary entrees, which correspond to each other.
        The Manhatten values are then sorted via Bubble sorting, while keeping their
        corresponding states, and the sorted list of successors is returned.
        '''

        # Obtaining the center coordinate of the board.
        # -- If odd (i.e. 5x5), the center is exact
        # -- If even (i.e. 4x4), we try to get as close to the "center" as possible
        x_center = int((self.b.size - 1) / 2)
        y_center = int((self.b.size - 1) / 2)

        heuristic_dict = {

            "value": [],
            "state": []
        }

        # Assigning Manhatten distances to the board states
        for successor in successors:

            distance = 0       

            for curr_x in range(self.b.size):

                for curr_y in range(self.b.size):

                    if successor[curr_x][curr_y] == '1':

                        # Formula for Manhatten distance
                        distance += abs(curr_x - x_center) + abs(curr_y - y_center)
            
            heuristic_dict["value"].append(distance)
            heuristic_dict["state"].append(successor)

        length = len(successors)

        for i in range(len(heuristic_dict["value"])):

            heuristic_dict["value"][i] += self.pathCost(heuristic_dict["state"][i])
            
        for i in range(length - 1):

            swapped = False

            for j in range(length - 1):
                
                # Using Bubble sorting to arange the states by least Manhatten distance
                if heuristic_dict["value"][j] > heuristic_dict["value"][j+1]:

                    tempState = heuristic_dict["state"][j]
                    tempValue = heuristic_dict["value"][j]

                    heuristic_dict["state"][j] = heuristic_dict["state"][j+1]
                    heuristic_dict["value"][j] = heuristic_dict["value"][j+1]

                    heuristic_dict["state"][j+1] = tempState
                    heuristic_dict["value"][j+1] = tempValue

                    swapped = True

            # If there are no more moves to be made, exit 
            if not swapped:

                break

        return heuristic_dict["state"]

    
    def pathCost(self, currentState):

        '''Takes in a successor state and calculates the cost of a path.'''

        init_pegs = (self.b.size ** 2) - 1
        curr_pegs = 0
        
        for i in range(self.b.size):
            
            curr_pegs += currentState[i].count('1')

        return abs(curr_pegs - init_pegs)


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