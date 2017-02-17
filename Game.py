"""
here's my main runner
"""
from Board import Board


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

print_legal_moves_test()

