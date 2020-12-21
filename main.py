import sys

from breadth import Breadth
from depth import Depth
from greedy import Greedy
from a_star import A_Star

def main():

    '''Runs a search algorithm if an user's arguement is valid.'''

    try:

        if sys.argv[1].lower() == 'breadth':

            breadth = Breadth()
            breadth.generate()

        elif sys.argv[1].lower() == 'depth':

            # Need because the successor function is recursively called
            sys.setrecursionlimit(10**8)

            depth = Depth()
            depth.generate()

        elif sys.argv[1].lower() == 'greedy':

            # Need because the successor function is recursively called
            sys.setrecursionlimit(10**8)

            greedy = Greedy()
            greedy.generate()

        elif sys.argv[1].lower() == 'a_star':

            a_star = A_Star()
            a_star.generate()

        else:

            print('\n-- Invalid argument entered, see the README file. --\n')

    except IndexError:

        print('''
- This program needs a command-line arguement to know which algorithm to run! --
            -- Please see the README file for instructions. --\n''')


if __name__ == '__main__':

    main()
