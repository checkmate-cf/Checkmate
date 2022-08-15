import board
import re


def welcome_user():
    pass


def move_piece(current_color, start_pos, end_pos):
    pass


def parse_input(user_input):
    """
    Checks to see if user_input valid within confines of chess space and desired format, then return tuple with start_pos
    and end_pos. Returns False if invalid user_input.

    :param user_input: format "D2 D3"
    :return: tuple(D2, D3)
    """
    split_input = user_input.split()
    if len(split_input) != 2:
        return False
    for pos in split_input:
        pattern = r"^[A-H][1-8]$"
        if not re.match(pattern, pos):
            return False
    return tuple(split_input)


def validate_move(piece, start_pos, end_pos, board):

    def validate_pawn(color, start_pos, end_pos, board):
        pass

    def validate_rook(start_pos, end_pos, board):
        pass

    def validate_king(start_pos, end_pos, board):
        pass

    def validate_queen(start_pos, end_pos, board):
        pass

    def validate_bishop(start_pos, end_pos, board):
        pass

    def validate_knight(start_pos, end_pos, board):
        pass

    if piece[1] == "Q":
        return validate_queen(start_pos, end_pos, board)
    elif piece[1] == "r":
        return validate_rook(start_pos, end_pos, board)
    elif piece[1] == "K":
        return validate_king(start_pos, end_pos, board)
    elif piece[1] == "b":
        return validate_bishop(start_pos, end_pos, board)
    elif piece[1] == "k":
        return validate_knight(start_pos, end_pos, board)
    elif piece == "{p}":
        return validate_pawn("black", start_pos, end_pos, board)
    elif piece == "[p]":
        return validate_pawn("white", start_pos, end_pos, board)


def check_check(color, board):
    pass


def check_checkmate(color, board):
    pass


def pawn_promotion(end_pos):
    pass


def reset(board):
    board.__init__()

