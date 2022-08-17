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