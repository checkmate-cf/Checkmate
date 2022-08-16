from board import Chessboard

def welcome_user():
    pass


def move_piece(current_color, start_pos, end_pos):
    pass


def parse_input(user_input):
    pass


def validate_move(start_pos, end_pos, board, player_color):
    # turn string input into array coordinates
    start_list = list(start_pos)
    end_list = list(end_pos)
    start_coord = [ord(start_list[0] - 65), 7 - (int(start_list[1])-1)]
    end_coord = [ord(end_list[0] - 65), 7 - (int(end_list[1])-1)]


    # validate piece color is same as player color
    def check_color(color):
        # get color of piece at start_pos
        piece_color = "white"
        if board[start_coord[1]][start_coord[0]][0] == "{":
            piece_color = "black"
        if color == piece_color:
            return True
        else:
            return False


    def validate_pawn(color, start_pos, end_pos, board):
        pass

    def validate_rook(start_pos, end_pos, board):
        # same column
        if start_pos[0] == end_pos[0]:
            spaces = abs(start_pos[1] - end_pos[1])
            # check if moving down
            if start_pos[1] - end_pos[1] < 0:
                row = start_pos[1] + 1
                col = start_pos[0]
                while spaces > 0:
                    if board[row][col] != "x":
                        return False
                    row += 1
                    spaces -= 1
                return True
            # moving up
            row = start_pos[1] - 1
            col = start_pos[0]
            while spaces > 0:
                if board[row][col] != "x":
                    return False
                row -= 1
                spaces -= 1
            return True

        # same row
        if start_pos[1] == end_pos[1]:
            spaces = abs(start_pos[0] - end_pos[0])
            # check if moving right
            if start_pos[0] - end_pos[0] < 0:
                row = start_pos[1]
                col = start_pos[0] + 1
                while spaces > 0:
                    if board[row][col] != "x":
                        return False
                    col += 1
                    spaces -= 1
                return True
            # moving left
            row = start_pos[1]
            col = start_pos[0] - 1
            while spaces > 0:
                if board[row][col] != "x":
                    return False
                col -= 1
                spaces -= 1
            return True

        return False

    def validate_king(start_pos, end_pos, board):
        pass

    def validate_queen(start_pos, end_pos, board):
        if validate_rook(start_pos, end_pos, board) or validate_bishop(start_pos, end_pos, board):
            return True

        return False

    def validate_bishop(start_pos, end_pos, board):
        # check if diagonal
        if abs(start_pos[0] - end_pos[0]) != abs(start_pos[1] - end_pos[1]):
            return False
        spaces = abs(start_pos[0] - end_pos[0])
        # check if moving right
        if start_pos[1] - end_pos[1] < 0:
            # check if moving down
            if start_pos[0] - end_pos[0] < 0:
                row = start_pos[1] + 1
                col = start_pos[0] + 1
                while spaces > 0:
                    if board[row][col] != "x":
                        return False
                    col += 1
                    row += 1
                    spaces -=1
                return True
            # moving up
            else:
                row = start_pos[1] - 1
                col = start_pos[0] + 1
                while spaces > 0:
                    if board[row][col] != "x":
                        return False
                    col += 1
                    row -= 1
                    spaces -= 1
                return True

        # moving left
        else:
            # check if moving down
            if start_pos[0] - end_pos[0] < 0:
                row = start_pos[1] + 1
                col = start_pos[0] - 1
                while spaces > 0:
                    if board[row][col] != "x":
                        return False
                    col -= 1
                    row += 1
                    spaces -=1
                return True
            # moving up
            else:
                row = start_pos[1] - 1
                col = start_pos[0] - 1
                while spaces > 0:
                    if board[row][col] != "x":
                        return False
                    col -= 1
                    row -= 1
                    spaces -= 1
                return True


    def validate_knight(start_pos, end_pos, board):
        pass

    if piece[1] == "Q":
        return validate_queen(start_coord, end_coord, board)
    elif piece[1] == "r":
        return validate_rook(start_coord, end_coord, board)
    elif piece[1] == "K":
        return validate_king(start_coord, end_coord, board)
    elif piece[1] == "b":
        return validate_bishop(start_coord, end_coord, board)
    elif piece[1] == "k":
        return validate_knight(start_coord, end_coord, board)
    elif piece == "{p}":
        return validate_pawn("black", start_coord, end_coord, board)
    elif piece == "[p]":
        return validate_pawn("white", start_coord, end_coord, board)


def check_check(color, board):
    pass


def check_checkmate(color, board):
    pass


def pawn_promotion(end_pos):
    pass


def reset(board):
    board.__init__()

