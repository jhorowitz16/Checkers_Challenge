"""
here's my main runner
"""
from Board import Board

def blank_board_test():
    my_board = Board()
    my_board.display()

def init_board_test():
    my_board = Board()
    my_board.display()
    my_board.init_setup()
    my_board.display()


init_board_test()
