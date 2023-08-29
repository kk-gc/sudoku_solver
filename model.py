class Sudoku:

    def __init__(self, string):
        self.string = string
        self.string_zeroed = self.convert_empties_to_zeros()
        self.board = self.convert_string_to_board()

    def convert_empties_to_zeros(self):
        return self.string.replace(' ', '0')

    def convert_string_to_board(self):
        # convert string to list of lists (rows)
        lol = [list(self.string_zeroed[i:i + 9]) for i in range(0, len(self.string_zeroed), 9)]
        # convert all list elements type form str to int
        board = [[int(el) for el in x] for x in lol]
        return board

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True
        else:
            row, col = empty

        for i in range(1, 10):
            if self.valid(i, row, col):
                self.board[row][col] = i
                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

    def valid(self, num, row, col):
        # Check row
        for i in range(9):
            if self.board[row][i] == num and col != i:
                return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num and row != i:
                return False

        # Check box
        box_x = col // 3
        box_y = row // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != (row, col):
                    return False
        return True




