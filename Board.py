"""
Represent the board as a 8 by 8 array, full of checker objects
"""
from Checker import Checker

# constants here
SIZE = 8
X = 'X'
O = 'O'
UR = 'UR'
UL = 'UL'
DR = 'DR'
DL = 'DL'
BLANK = '_'

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

    def get_X_moves(self):
        """
        just get the moves
        """
        moves = []
        for i in range(SIZE):
            for j in range(SIZE):
                if self.d_board[i][j] == X:
                    if i < SIZE-1 and j > 0 and not self.h_board[i+1][j-1]:
                        moves.append(((i, j), 'DL'))
                    if i < SIZE-1 and j < SIZE-1 and not self.h_board[i+1][j-1]:
                        moves.append(((i, j), 'DR'))
        return moves
        
    def get_O_moves(self):
        """
        just get the moves
        """
        moves = []
        for i in range(SIZE):
            for j in range(SIZE):
                if self.d_board[i][j] == O:
                    if i > 0 and j > 0 and not self.h_board[i-1][j-1]:
                        moves.append(((i, j), 'UL'))
                    if i > 0 and j < SIZE-1 and not self.h_board[i-1][j+1]:
                        moves.append(((i, j), 'UR'))
        return moves

    def enumerate_moves(self, moves):
        """
        take a set of legal moves, and number them off with letters
        """
        print("Where would you like to move?")
        curr = 65  # capital A 
        for move in moves:
            print(chr(curr) + ") Piece at " + str(move[0]) + " " + str(move[1]) + "?")
            curr += 1
            

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

    def make_move(self, move, team):
        """
        make the move here - where move is a starting coordinate and a direction tuple
        """
        s = move[0]  # starting tuple x,y
        direction = move[1]  # UR UL DR or DL

        # get the piece at the sing location, then move it
        # remember to update both hidden and display
        piece = self.h_board[s[0]][s[1]]
        a = s[0]
        b = s[1]
        if not piece:
            print("NO PIECE FOUND, INVALID MOVE")
        else:
            self.h_board[a][b] = None
            self.d_board[a][b] = BLANK 
            if direction == UR:
                self.h_board[a-1][b+1] = piece
                self.d_board[a-1][b+1] = team
            elif direction == UL:
                self.h_board[a-1][b-1] = piece
                self.d_board[a-1][b-1] = team
            elif direction == DR:
                self.h_board[a+1][b+1] = piece
                self.d_board[a+1][b+1] = team
            elif direction == DL:
                self.h_board[a+1][b-1] = piece
                self.d_board[a+1][b-1] = team
            else:
                print("BAD DIRECTION, INVALID MOVE")
                
        

    # utils

    def __repr__(self):
        return self.name + " | " + str(self.h_board)

    def __str__(self):
        return str(self.d_board)

        


