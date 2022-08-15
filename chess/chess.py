import board


def welcome_user():
    pass


def move_piece(current_color, start_pos, end_pos):
    pass


def parse_input(user_input):
    pass


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

