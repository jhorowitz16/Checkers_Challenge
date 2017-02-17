"""
here's my main runner
"""
from Board import Board

# core functions here

def play_game():

    board = start()
    valid = True
    count = 0
    while valid:
        print("Round number: " + str(count))
        O_turn(board)
        X_turn(board)
        count += 1


def O_turn(mb):
    """
    take a single turn for the 'O' player
    """
    moves = mb.get_O_moves()
    mb.enumerate_moves(moves)
    selection = ''
    while not selection:
        selection = raw_input("Select a move for the 'O' player: ")
        # screen the input later...
        if not selection:
            print("BAD INPUT")
    index = ord(selection[0].upper()) - 65
    if index >= 0 and index < len(moves):
        move = moves[index]
        print("You have selected: " + str(move))
        mb.make_move(move, 'O')
    else:
        print("INVALID MOVE")
    mb.display()


def X_turn(mb):
    """
    take a single turn for the 'O' player
    """
    moves = mb.get_X_moves()
    mb.enumerate_moves(moves)
    selection = ''
    while not selection:
        selection = raw_input("Select a move for the 'X' player: ")
        # screen the input later...
        if not selection:
            print("BAD INPUT")
    # screen the input later...
    index = ord(selection[0].upper()) - 65
    if index >= 0 and index < len(moves):
        move = moves[index]
        print("You have selected: " + str(move))
        mb.make_move(move, 'X')
    else:
        print("INVALID MOVE")
    mb.display()









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


# Run the game! :) 
play_game()
