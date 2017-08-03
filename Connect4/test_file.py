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
        game1 = ConnectFour(1, "Jerry", difficulty = 1, board=board1)
        game1.num_empty = 30
        for direction in ["vertical", "horiziontal", "LD", "RD"]:
            res = game1.line_check("X", "horizontal", 3)
            self.assertFalse(res)
