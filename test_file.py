import unittest

from connect_four import *

class TestGame(unittest.TestCase):

    def test_linecheck_1(self):
        board1 = [[ ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [ ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                  [ ' ', ' ', 'O', ' ', ' ', ' ', ' '],
                  [ ' ', 'O', 'X', 'O', 'O', ' ', ' '],
                  [ ' ', 'X', 'X', 'O', 'X', ' ', ' '],
                  [ 'X', 'O', 'X', 'X', 'O', 'O', 'O']]
