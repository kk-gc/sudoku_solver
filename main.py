from model import SudokuData, SudokuImageRecognizer
from view import SudokuView

import re


class SudokuController:

    def __init__(self):
        self._view = SudokuView()
        self.sudoku_to_solve = None
        self.raw_user_input = self._view.get_user_input()
        self.valid_user_input = self.validate_user_input()

        self.sudoku = self.sudoku_make()

    def validate_user_input(self):
        _option_chosen, _data = self.raw_user_input

        # option 1 - from sudoku string:
        if _option_chosen == 1:
            # _data should be 9 x 9 = 81 and contains only numbers 1-9 or empty spaces ' '
            if len(_data) == 81 and re.match(r'[1-9 ]{81}', _data):
                self.sudoku_to_solve = _data
                return True
            return False

        # option 2 - from sudoku file image:
        elif _option_chosen == 2:
            sir = SudokuImageRecognizer(_data)
            if sir.best_result:
                self.sudoku_to_solve = sir.best_result
                return True

        # option 3 - exit:
        else:
            self.print_exit_message()
            return False

    def sudoku_make(self):
        if self.sudoku_to_solve:
            return SudokuData(self.sudoku_to_solve)
        return None

    def print_something_went_wrong(self):
        self._view.print_something_went_wrong()

    def print_solved_sudoku_as_board(self):
        self._view.print_as_board(self.sudoku.board)

    def print_exit_message(self):
        self._view.print_exit_message()


if __name__ == '__main__':

    sc = SudokuController()

    if sc.sudoku and sc.sudoku.board:
        sc.print_solved_sudoku_as_board()
    else:
        sc.print_something_went_wrong()
