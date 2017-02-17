"""
Represent the board as a 8 by 8 array, full of checker objects
"""
from Checker import Checker

# constants here
SIZE = 8
X = 'X'
O = 'O'

class Board:
    

    def __init__(self, name="my_board"):
        self.checkers = []
        self.name = name

        # build the two lineups
        self.X_team = [Checker('X', id) for id in range(12)]
        self.O_team = [Checker('O', id) for id in range(12)]

        # add the checkers to the board
        # regular d_board is for display and h_board is for hidden memory
        # _ for blank
        self.d_board = [['_' for _ in range(8)] for _ in range(8)]
        self.h_board = [[None for _ in range(8)] for _ in range(8)]

    def init_setup(self):
        """
        place all the checkers in their starting positions
        checkers can only go on the diagonal spots
            this is when row val plus col val is an odd numberk
                (indexing from 0)
        """

        # first half of the checkers!
        checker_counter = 0
        for i in range(3):
            for j in range(len(self.h_board[0])):
                if (i + j) % 2 == 1:
                    # odd number! add a checker
                    check = self.X_team[checker_counter]
                    checker_counter += 1
                    self.d_board[i][j] = 'X'
                    self.h_board[i][j] = check

        # second half of the checkers!
        checker_counter = 0
        for i in range(5, 8):
            for j in range(len(self.h_board[0])):
                if (i + j) % 2 == 1:
                    # odd number! add a checker
                    check = self.O_team[checker_counter]
                    checker_counter += 1
                    self.d_board[i][j] = 'O'
                    self.h_board[i][j] = check


    def display(self):
        print("\n\n  --------------------------------------------") 
        for row in self.d_board:
            ret_str = "  | "
            for spot in row:
                ret_str += " _" + spot + "_ "
            print(ret_str + " |")
        print("  --------------------------------------------\n\n")


    def print_legal_X_moves(self):
        """
        for the desired team, print all legal moves (not jumps)
        """
        print("\nLEGAL X MOVES")
        for i in range(SIZE):
            for j in range(SIZE):
                if self.d_board[i][j] == X:
                    # found a piece of this team
                    print("found a X at " + str((i, j)))
                    # Xs must move down, so check larger rows
                    # WATCH OUT not on the end
                    if i < SIZE-1 and j > 0 and not self.h_board[i+1][j-1]:
                        # below and left
                        print(" >>> downleft move available")
                    if i < SIZE-1 and j < SIZE-1 and not self.h_board[i+1][j-1]:
                        # below and right 
                        print(" >>> downright move available")
        

    def print_legal_O_moves(self):
        """
        for the desired team, print all legal moves (not jumps)
        """
        print("\nLEGAL O MOVES")
        for i in range(SIZE):
            for j in range(SIZE):
                if self.d_board[i][j] == O:
                    # found a piece of this team
                    print("found a O at " + str((i, j)))
                    # Os must move up, so check smaller rows
                    # WATCH OUT not on the end
                    if i > 0 and j > 0 and not self.h_board[i-1][j-1]:
                        # up and left
                        print(" >>> upleft move available")
                    if i > 0 and j < SIZE-1 and not self.h_board[i-1][j-1]:
                        # up and right 
                        print(" >>> upright move available")


    def __repr__(self):
        return self.name + " | " + str(self.h_board)

    def __str__(self):
        return str(self.d_board)

        


