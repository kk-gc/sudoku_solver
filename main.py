from model import SudokuData
from view import SudokuView


class SudokuController:

    def __init__(self):
        self._view = SudokuView()
        self.user_input = self._view.get_user_input()
        self.user_input_ok = self.user_input_validate()

        self.sudoku = self.sudoku_make()

    def user_input_validate(self):
        # user_input should be 9 x 9 = 81 characters long
        if len(self.user_input) != 81:
            return False

        try:
            # user_input should be a string with numbers and spaces only
            # so after removing spaces should be able to convert to integer
            int(self.user_input.replace(' ', ''))
        except ValueError:
            return False
        return True

    def sudoku_make(self):
        if self.user_input_ok:
            return SudokuData(self.user_input)
        return None

    # def sudoku_solve(self):
    #     if self.sudoku:
    #         self.sudoku.solve()
    #     return False

from controller import SudokuController


if __name__ == '__main__':

    controller = SudokuController()
    if controller.sudoku:
        controller._view.print_as_board(controller.sudoku.board)
    else:
        controller._view.print_something_went_wrong()
