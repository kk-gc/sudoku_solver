from model import SudokuData
from view import SudokuView


class SudokuController:

    def __init__(self):
        self._view = SudokuView()
        self.raw_user_input = self._view.user_input()
        self.user_input_ok = self.user_input_validate()

        self.sudoku = self.sudoku_make()

    def user_input_validate(self):
        # user_input should be 9 x 9 = 81 characters long
        if len(self.raw_user_input) != 81:
            return False

        try:
            # user_input should be a string with numbers and spaces only
            # so after removing spaces should be able to convert to integer
            int(self.raw_user_input.replace(' ', ''))
        except ValueError:
            return False
        return True

    def sudoku_make(self):
        if self._view.user_input_valid:
            return SudokuData(self._view.user_input)
        return None

    # def sudoku_solve(self):
    #     if self.sudoku:
    #         self.sudoku.solve()
    #     return False

