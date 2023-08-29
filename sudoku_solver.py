from controller import Controller


if __name__ == '__main__':

    controller = Controller()
    controller.sudoku_solve()
    controller.view.print_as_board(controller.sudoku.board)

