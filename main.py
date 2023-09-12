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

    def print_something_went_wrong(self):
        self._view.print_something_went_wrong()

    def print_solved_sudoku_as_board(self):
        self._view.print_as_board(self.sudoku.board)


if __name__ == '__main__':

    sc = SudokuController()

    if sc.sudoku and sc.sudoku.board:
        sc.print_solved_sudoku_as_board()
    else:
        sc.print_something_went_wrong()
