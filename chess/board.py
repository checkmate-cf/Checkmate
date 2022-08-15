class Chessboard:

    def __init__(self):
        self.board = [["{r}", "{k}", "{b}", "{Q}", "{K}", "{b}", "{k}", "{r}"],
                      ["{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}", "{p}"],
                      ["x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x"],
                      ["x", "x", "x", "x", "x", "x", "x", "x"],
                      ["[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]", "[p]"],
                      ["[r]", "[k]", "[b]", "[Q]", "[K]", "[b]", "[k]", "[r]"]]

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


if __name__ == "__main__":
    my_board = Chessboard()
    my_board.render()