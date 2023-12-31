# Added as pytest have some issues with importing
# relative path modules - known issue
import sys
import os
sys.path.insert(0, os.getcwd())

import pytest
import model


@pytest.mark.parametrize('raw_string, is_valid',
                         [('2 9  7      386972     9    6 75     53   86    6 85 4 9    4   2  65 19  79  6 3', True),
                          ('3      14 17346 894598 7 268 5 73    72     8   2  4     7 19 3 9  248  5       7', True),
                          ('913   42  8   4  525 1 96 3      5 8   658  2 3  9 7 4 4 9       6         4 7  6', True),
                          ('7    6  4  9       2   381 312    97     4 26   2      4 5      9 3   78   1  2  ', True),
                          ('  4  1  8        73  4     1  2 6  9    387   2     1  8 3   2  6  1     7     65', True),
                          ('2  8   7  9     3 1    49 8       9 4   5     1 3  6 2        7 6 2  8 1  2  3   ', True),
                          ])
def test_sudoku_data_validate_raw_strings_good(raw_string, is_valid):
    vs = model.SudokuData(raw_string).valid_string
    assert vs


@pytest.mark.parametrize('raw_string, is_valid',
                         [('2  8   7  9     3 1    49 8       9 4   5     1 3  6 2        7 6 2  8 1  2  3  ', False),
                          ('2  8   7  9     3 1    49 8       9 4   5     1 3  6 2        7 6 2  8 1  2  3  a', False),
                          ('-2  8   7  9     3 1    49 8       9 4   5     1 3  6 2        7 6 2  8 1  2  3  ', False),
                          (28793149894513627628123, False),
                          (-28793149894513627628123, False),
                          ('200800070090000030100004908000000090400050000010300602000000007060200801002003000', False),
                          (200800070090000030100004908000000090400050000010300602000000007060200801002003000, False),
                          (-200800070090000030100004908000000090400050000010300602000000007060200801002003000, False),
                          ])
def test_sudoku_data_validate_raw_strings_bad(raw_string, is_valid):
    vs = model.SudokuData(raw_string).valid_string
    assert not vs


@pytest.mark.parametrize('raw_string_valid, raw_string_zeroed',
                         [('2 9  7      386972     9    6 75     53   86    6 85 4 9    4   2  65 19  79  6 3',
                           '209007000000386972000009000060750000053000860000608504090000400020065019007900603'),
                          ('3      14 17346 894598 7 268 5 73    72     8   2  4     7 19 3 9  248  5       7',
                           '300000014017346089459807026805073000072000008000200400000701903090024800500000007'),
                          ('913   42  8   4  525 1 96 3      5 8   658  2 3  9 7 4 4 9       6         4 7  6',
                           '913000420080004005250109603000000508000658002030090704040900000006000000000407006'),
                          ('7    6  4  9       2   381 312    97     4 26   2      4 5      9 3   78   1  2  ',
                           '700006004009000000020003810312000097000004026000200000040500000090300078000100200'),
                          ('  4  1  8        73  4     1  2 6  9    387   2     1  8 3   2  6  1     7     65',
                           '004001008000000007300400000100206009000038700020000010080300020060010000070000065'),
                          ('2  8   7  9     3 1    49 8       9 4   5     1 3  6 2        7 6 2  8 1  2  3   ',
                           '200800070090000030100004908000000090400050000010300602000000007060200801002003000'),
                          ])
def test_sudoku_data_empties_to_zeroes(raw_string_valid, raw_string_zeroed):
    sz = model.SudokuData(raw_string_valid).string_zeroed
    assert sz == raw_string_zeroed


@pytest.mark.parametrize('raw_string_valid',
                         ['2 9  7      386972     9    6 75     53   86    6 85 4 9    4   2  65 19  79  6 3',
                          '3      14 17346 894598 7 268 5 73    72     8   2  4     7 19 3 9  248  5       7',
                          '913   42  8   4  525 1 96 3      5 8   658  2 3  9 7 4 4 9       6         4 7  6',
                          '7    6  4  9       2   381 312    97     4 26   2      4 5      9 3   78   1  2  ',
                          '  4  1  8        73  4     1  2 6  9    387   2     1  8 3   2  6  1     7     65',
                          '2  8   7  9     3 1    49 8       9 4   5     1 3  6 2        7 6 2  8 1  2  3   ',
                          ])
def test_sudoku_data_string_to_board(raw_string_valid):
    board = model.SudokuData(raw_string_valid).board
    assert isinstance(board, list)
    assert len(board) == 9
    assert all([len(row) == 9 for row in board])    # all rows length = 9 ?
    assert all([all([isinstance(number, int) for number in row]) for row in board])     # all rows contain only integers
