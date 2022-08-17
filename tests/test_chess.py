import pytest
import chess.chess as c
import chess.board as b


# @pytest.mark.skip("pending")
def test_move_white_pawn_one():
    board = b.Chessboard()
    actual = c.validate_move("A2", "A3", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_white_pawn_two():
    board = b.Chessboard()
    actual = c.validate_move("A2", "A4", board, "white")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_white_pawn_one_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
             ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["[Q]", "x", "x", "x", "x", "x", "x", "x"],
             ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
             ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A2", "A3", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_white_pawn_two_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
             ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["[Q]", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
             ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A2", "A4", board, "white")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_black_pawn_one():
    board = b.Chessboard()
    actual = c.validate_move("A7", "A6", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_black_pawn_two():
    board = b.Chessboard()
    actual = c.validate_move("A7", "A5", board, "black")
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_black_pawn_one_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
             ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
             ["[Q]", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
             ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A7", "A6", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_black_pawn_two_blocked():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
             ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["[Q]", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
             ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A7", "A5", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_white_pawn_two_not_home():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
             ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["[p]", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
             ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A3", "A5", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_black_pawn_two_not_home():
    board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
             ["x", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
             ["{p}", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["x", "x", "x", "x", "x", "x", "x", "x"],
             ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
             ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    actual = c.validate_move("A7", "A5", board, "black")
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_pawn(standard_board):
    actual = standard_board.board
    c.move_piece("A2", "A3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["[p]",  "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",  "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_knight(standard_board):
    actual = standard_board.board
    c.move_piece("B1", "C3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x", "[k]",   "x",   "x",   "x",   "x",   "x"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["[r]",  "x",  "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_rook(pawns_forward_board):
    actual = pawns_forward_board.board
    c.move_piece("A1", "A3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["[r]",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_bishop(pawns_forward_board):
    actual = pawns_forward_board.board
    c.move_piece("C1", "A3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["[b]",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                ["[r]", "[k]", "x", "[Q]", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_queen(pawns_forward_board):
    actual = pawns_forward_board.board
    c.move_piece("D1", "F3", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["x", "x", "x", "x", "x", "[Q]", "x", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["[r]", "[k]", "[b]", "x", "[K]", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_move_king(pawns_forward_board):
    actual = pawns_forward_board.board
    c.move_piece("E1", "E2", actual, False)
    expected = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                ["x", "x", "x", "x", "x", "x", "x", "x"],
                ["x", "x", "x", "x", "[K]", "x", "x", "x"],
                ["[r]", "[k]", "[b]", "[Q]", "x", "[b]", "[k]", "[r]"]]
    assert actual == expected


# @pytest.mark.skip("pending")
def test_black_king_not_check(standard_board):
    actual = c.check_check("black", standard_board)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_black_king_check(black_in_check_not_checkmate):
    actual = c.check_check("black", black_in_check_not_checkmate)
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_black_king_check_not_checkmate(black_in_check_not_checkmate):
    actual = c.check_checkmate("black", black_in_check_not_checkmate)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_white_king_checkmate(white_in_checkmate):
    actual = c.check_checkmate("white", black_in_checkmate)
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_white_king_not_check(standard_board):
    actual = c.check_check("white", standard_board)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_white_king_check(white_in_check_not_checkmate):
    actual = c.check_check("white", white_in_check_not_checkmate)
    expected = True
    assert actual == expected


# @pytest.mark.skip("pending")
def test_white_king_check_not_checkmate(white_in_check_not_checkmate):
    actual = c.check_checkmate("white", white_in_check_not_checkmate)
    expected = False
    assert actual == expected


# @pytest.mark.skip("pending")
def test_white_king_checkmate(white_in_checkmate):
    actual = c.check_checkmate("white", white_in_checkmate)
    expected = True
    assert actual == expected

@pytest.fixture
def standard_board():
    standard_board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                                   ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                                   ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                   ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                   ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                   ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                   ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                                   ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    return standard_board

@pytest.fixture
def black_in_checkmate():
    black_in_checkmate = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                                                 ["x",   "{p}", "{p}", "{p}", "{p}", "[Q]", "{p}", "{p}"],
                                                 ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                                 ["{p}",  "x",  "[b]",  "x",   "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",  "[p]",  "x",   "x",   "x"],
                                                 ["[p]", "[p]", "[p]", "[p]",  "x",  "[p]", "[p]", "[p]"],
                                                 ["[r]", "[k]", "[b]",  "x", "[K]",  "x", "[k]", "[r]"]])
    return black_in_checkmate


@pytest.fixture
def pawns_forward_board():
    pawns_forward_board = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                                        ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                        ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                        ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                                        ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                                        ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                        ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                        ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    return pawns_forward_board

@pytest.fixture
def black_in_check_not_checkmate():
    black_in_check_not_checkmate = b.Chessboard([["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                                                 ["x",  "{p}", "{p}", "{p}", "{p}", "[Q]", "{p}", "{p}"],
                                                 ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                                 ["{p}",  "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",  "[p]",  "x",   "x",   "x"],
                                                 ["[p]", "[p]", "[p]", "[p]",   "x", "[p]", "[p]", "[p]"],
                                                 ["[r]", "[k]", "[b]",  "x", "[K]", "[b]", "[k]", "[r]"]])
    return black_in_check_not_checkmate


@pytest.fixture
def white_in_check_not_checkmate():
    white_in_check_not_checkmate = b.Chessboard([["{r}", "{k}", "{b}",   "x" , "{K}", "{b}", "{k}", "{r}"],
                                                 ["{p}",  "{p}", "{p}", "{p}", "x"  , "{p}", "{p}", "{p}"],
                                                 ["x",    "[p]", "x",   "x",   "{p}", "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                                 ["x",    "x",   "x",   "x",    "x",  "x",   "x",   "x"],
                                                 ["[p]", "x"  , "[p]", "[p]", "[p]", "{Q}", "[p]","[p]"],
                                                 ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    return white_in_check_not_checkmate

@pytest.fixture
def white_in_checkmate():
    white_in_checkmate = b.Chessboard([["{r}", "{k}", "{b}",   "x" , "{K}", "x"  , "{k}", "{r}"],
                                       ["{p}",  "{p}", "{p}", "{p}", "x"  , "{p}", "{p}", "{p}"],
                                       ["x",    "[p]", "x",   "x",   "{p}", "x",   "x",   "x"],
                                       ["x",    "x",   "{b}", "x",   "x",   "x",   "x",   "x"],
                                       ["x",    "x",   "x",   "x",   "x",   "x",   "x",   "x"],
                                       ["x",    "x",   "[p]", "x",    "x",  "x",   "x",   "x"],
                                       ["[p]", "x"  , "x"  , "[p]", "[p]", "{Q}", "[p]","[p]"],
                                       ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]])
    return white_in_checkmate
