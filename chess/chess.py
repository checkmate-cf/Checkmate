from board import Chessboard
import re
import copy


def welcome_user():
    print("Welcome to Checkmate, the ultimate destination for playing chess!")
    print("Would you like to play chess? y/n ")
    user_input = input("> ").lower()
    while user_input != "y" and user_input != "n":
        print('Must enter valid response: "y" or "n", try again')
        input("> ")
    return user_input == "y"


def move_piece(start_pos, end_pos, board, real_move=True):
    start_pos = (7 - (int(start_pos[1]) - 1), ord(start_pos[0]) - 65)
    end_pos = (7 - (int(end_pos[1]) - 1), ord(end_pos[0]) - 65)
    moving_piece = board[start_pos[0]][start_pos[1]]
    moving_piece_color = None
    if moving_piece[0] == "[":
        moving_piece_color = True  # True == "white"
    elif moving_piece[0] == "{":
        moving_piece_color = False  # False == "black"
    board[start_pos[0]][start_pos[1]] = "x"
    board[end_pos[0]][end_pos[1]] = moving_piece
    if real_move:
        if moving_piece[1] == "p":
            if moving_piece_color and end_pos[0] == 0:
                pawn_promotion(end_pos[1], board, moving_piece_color)
            if not moving_piece_color and end_pos[0] == 7:
                pawn_promotion(end_pos[1], board, moving_piece_color)


def parse_input(user_input):
    """
    Checks to see if user_input valid within confines of chess space and desired format, then return tuple with start_pos
    and end_pos. Returns False if invalid user_input.

    :param user_input: format "D2 D3"
    :return: tuple(D2, D3)
    """
    split_input = user_input.upper().split()
    if len(split_input) != 2:
        return False
    if split_input[0] == split_input[1]:
        return False
    for pos in split_input:
        pattern = r"^[A-H][1-8]$"
        if not re.match(pattern, pos):
            return False
    return tuple(split_input)


def check_check(color, board, move=None):
    def find_king(color, copied_board):
        for row_idx, row in enumerate(copied_board.board):
            for col_idx, col_val in enumerate(row):
                if color:
                    if col_val == "[K]":
                        return row_idx, col_idx
                else:
                    if col_val == "{K}":
                        return row_idx, col_idx

    copied_board = copy.deepcopy(board)
    if move:
        move_piece(move[0], move[1], copied_board.board, False)
    king_loc = find_king(color, copied_board)
    for row_idx, row in enumerate(copied_board.board):
        for col_idx, col_val in enumerate(row):
            if color and col_val[0] == "{":
                start_pos_text = f"{chr(row_idx + 65)}{8 - col_idx}"
                end_pos_text = f"{chr(king_loc[0] + 65)}{8 - king_loc[1]}"
                validate_move(start_pos_text, end_pos_text, copied_board)
            elif not color and col_val[0] == "[":
                start_pos_text = f"{chr(row_idx + 65)}{8 - col_idx}"
                end_pos_text = f"{chr(king_loc[0] + 65)}{8 - king_loc[1]}"
                validate_move(start_pos_text, end_pos_text, copied_board)


def check_checkmate(color, board):
    pass


def pawn_promotion(end_col, board, curr_color):
    print('PAWN PROMOTION: What piece would you like to promote to? ("Q", "r", "b", "k")')
    promotion_type = input("> ")
    while promotion_type != "Q" and promotion_type != "r" and promotion_type != "b" and promotion_type != "k":
        print('Please enter valid input ("Q", "r", "b", "k")')
        promotion_type = input("> ")
    if curr_color:
        board[0][end_col] = f"[{promotion_type}]"
    else:
        board[7][end_col] = f"{{{promotion_type}}}"

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


def reset(board):
    board.__init__()


def play_game():
    if welcome_user():
        game_board = Chessboard()
        game_not_over = True
        curr_player = "White"
        while game_not_over:
            game_board.render()
            print(f"{curr_player}'s turn")
            valid_move = False
            while not valid_move:
                user_input = input("Where would you like to move: ")
                parsed_input = parse_input(user_input)
                if not parsed_input:
                    print('Please answer in the format "B2 B3". Must be in range A-H and 1-8')
                # elif not validate_move(valid_parsed_input[0], valid_parsed_input[1], game_board, curr_player.lower):
                #     print('Move not possible')
                elif check_check(curr_player, game_board, parsed_input):
                    print("You may not cause your own king to be put in check")
                else:
                    valid_move = True
                    move_piece(parsed_input[0], parsed_input[1], game_board.board)
            if curr_player == "White":
                curr_player = "Black"
            elif curr_player == "Black":
                curr_player = "White"


play_game()
