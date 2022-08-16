class Chessboard:

    def __init__(self, board=None):
        if board is not None:
            self.board = board
        else:
            self.board = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                          ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["x", "x", "x", "x", "x", "x", "x", "x"],
                          ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                          ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]]

    def __deepcopy__(self, memodict={}):
        copied_board = []
        for row_idx, row in enumerate(self.board):
            copied_board.append([])
            for col_val in row:
                copied_board[row_idx].append(col_val)
        return Chessboard(copied_board)

    def render(self):
        for i in range(8):
            print(f"   {chr(65 + i)}", end="")
        print()
        for row_idx, row in enumerate(self.board):
            print(f"{8 - row_idx}|", end="")
            for col_idx, col_val in enumerate(row):
                if col_val == "x":
                    col_val = " x "
                if col_idx != 7:
                    print(f"{col_val} ", end="")
                else:
                    print(col_val, end="")
            print(f"|{8 - row_idx}")
        for i in range(8):
            print(f"   {chr(65 + i)}", end="")
        print()
