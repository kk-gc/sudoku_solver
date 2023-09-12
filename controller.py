from model import SudokuData
from view import SudokuView


class SudokuController:

    def __init__(self):
        self._view = SudokuView()
        self.raw_user_input = self._view.user_input()
        self.sudoku = self.sudoku_make()

    def sudoku_make(self):
        if self._view.user_input_valid:
            return SudokuData(self._view.user_input)
        return None

    # def sudoku_solve(self):
    #     if self.sudoku:
    #         self.sudoku.solve()
    #     return False

