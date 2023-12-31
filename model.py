import datetime
import re
from sudoku_image_recognizer import SudokuImageRecognizer
from typing import Optional


class SudokuData:

    def __init__(self, raw_string):
        self.raw_string = raw_string
        self.valid_string = self.validate_raw_string()
        self.string_zeroed = self._convert_empties_to_zeros()
        self.board = self._convert_string_to_board()

        self.solve_sudoku()

    def validate_raw_string(self) -> str | bool:
        if isinstance(self.raw_string, str) \
                and len(self.raw_string) == 81 \
                and re.match(r'[1-9 ]{81}', self.raw_string):
            return self.raw_string
        return False

    def _convert_empties_to_zeros(self) -> Optional[str]:
        if self.valid_string:
            return self.valid_string.replace(' ', '0')
        return None

    def _convert_string_to_board(self) -> Optional[list[list]]:
        if self.string_zeroed:
            # convert string to list of lists (rows)
            lol = [list(self.string_zeroed[i:i + 9]) for i in range(0, len(self.string_zeroed), 9)]
            # convert all list elements type form str to int
            board = [[int(el) for el in x] for x in lol]
            return board
        return None

    def solve_sudoku(self) -> None:
        if self.board:
            sa = SudokuAlgorithm(self.board)
            if sa.board_solved_ok:
                self.board = sa.board
            else:
                self.board = None


class SudokuAlgorithm:

    def __init__(self, board, timeout=5):
        self.algorithm_start = datetime.datetime.now()
        self.board = board
        self.timeout = timeout

        # True if solved, False is timeout
        self.board_solved_ok = self._solve()

    def _solve(self) -> bool:
        # timeout:
        if (datetime.datetime.now() - self.algorithm_start).seconds > self.timeout:
            return False

        empty = self._find_empty()
        if not empty:
            return True
        else:
            row, col = empty

        for i in range(1, 10):
            if self._valid(i, row, col):
                self.board[row][col] = i
                if self._solve():
                    return True
                self.board[row][col] = 0
        return False

    def _find_empty(self) -> Optional[tuple[int, int]]:
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None

    def _valid(self, num: int, row: int, col: int) -> bool:
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
