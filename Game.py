"""
here's my main runner
"""
from Board import Board

# helpers
def start():
    mb = Board()
    mb.init_setup()
    mb.display()
    return mb

# phase one testing

def blank_board_test():
    my_board = Board()
    my_board.display()

def init_board_test():
    my_board = Board()
    my_board.display()
    my_board.init_setup()
    my_board.display()


# phase two testing
def print_legal_moves_test():
    mb = Board()
    mb.init_setup()
    mb.display()
    mb.print_legal_X_moves()
    mb.print_legal_O_moves()

def user_selects_move_test():
    start()
    Os = mb.get_O_moves()
    Xs = mb.get_X_moves()
    print(Os)
    print(Xs)
    
def O_first_move_test():
    mb = start()
    moves = mb.get_O_moves()
    mb.enumerate_moves(moves)
    selection = raw_input("Select a move: ")
    # screen the input later...
    index = ord(selection[0].upper()) - 65
    if index >= 0 and index < len(moves):
        move = moves[index]
        print("You have selected: " + str(move))
        mb.make_move(move, 'O')
    else:
        print("INVALID MOVE")
    mb.display()



O_first_move_test()


