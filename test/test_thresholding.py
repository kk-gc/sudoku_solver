# Added as pytest have some issues with importing
# relative path modules - known issue
import sys
import os
sys.path.insert(0, os.getcwd())

import pytest
import thresholding
import cv2


def test_thresholding_image_good():
    image = cv2.imread('./sudoku.png')
    t = thresholding.thresholding(image, show_results=False)
    assert isinstance(t, dict)


def test_thresholding_image_good_results_bad():
    image = cv2.imread('./sudoku.png')
    show_results = None
    t = thresholding.thresholding(image, show_results=show_results)
    assert t is None


def test_thresholding_image_bad():
    image = str('1234')
    t = thresholding.thresholding(image, show_results=False)
    assert t is None

