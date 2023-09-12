from model import SudokuData
from view import View


class Controller:

    def __init__(self):
        self.view = View()
        self.sudoku = self.sudoku_make()

    def sudoku_make(self):
        if self.view.user_input_valid:
            return SudokuData(self.view.user_input)
        return None

    # def sudoku_solve(self):
    #     if self.sudoku:
    #         self.sudoku.solve()
    #     return False

