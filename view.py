class SudokuView:

    def __init__(self):
        self.user_input = self.get_user_input()
        self.user_input_valid = self.user_input_validate()

    def get_user_input(self):
        return input('sudoku: ')

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

    @staticmethod
    def print_as_board(board):
        SEPARATOR_VERTICAL = '|'
        SEPARATOR_HORIZONTAL = '='

        for row in range(9):

            _1st = ''.join([str(el) for el in board[row][:3]])
            _2nd = ''.join([str(el) for el in board[row][3:6]])
            _3rd = ''.join([str(el) for el in board[row][6:]])
            line = ' '.join(f'{_1st}{SEPARATOR_VERTICAL}'
                            f'{_2nd}{SEPARATOR_VERTICAL}'
                            f'{_3rd}')
            if row and row / 3 == row // 3:
                print(SEPARATOR_HORIZONTAL * 21)

            print(line)

    @staticmethod
    def print_something_went_wrong():
        print('Something went wrong.')

