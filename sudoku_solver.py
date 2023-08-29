from controller import Controller


if __name__ == '__main__':

    controller = Controller()
    if controller.sudoku:
        controller.view.print_as_board(controller.sudoku.board)
    else:
        controller.view.print_something_went_wrong()
