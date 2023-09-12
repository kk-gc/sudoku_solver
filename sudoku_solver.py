from controller import SudokuController


if __name__ == '__main__':

    controller = SudokuController()
    if controller.sudoku:
        controller.view.print_as_board(controller.sudoku.board)
    else:
        controller.view.print_something_went_wrong()
