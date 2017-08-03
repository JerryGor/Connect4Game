"""
University Of Toronto CSC384 Introduction to AI
Final Procject: Connect4
MiniMax, AlphaBeta Prunning and Game Search Tree

Lester Lyu
Jonathan Yan
Jerry Yi

August 10, 2017
"""
import copy

# default name
PLAYER_1 = "Player1"
PLAYER_2 = "Player2"
COMPUTER_NAME = "COMPUTER"
AI_1 = "SIRI"
AI_2 = "CORTANA"

# difficulty
EASY = 6

# Game
NUM_ROWS = 6
NUM_COLS = 7
EMPTY_SLOT = " "
TOKEN_1 = "X"
TOKEN_2 = "O"


class ConnectFour:
    def __init__(self, mode=1, p1=PLAYER_1, p2=PLAYER_2, difficulty=EASY, num_rows=NUM_ROWS, num_cols=NUM_COLS,
                 board=None):
        """
        initialize a ConnectFour game.

        :parm mode: 1 is single player
        :parm mode: 2 is double player
        :parm mode: 3 is ai vs ai

        :parm p1: name of player 1
        :parm p2: name of player 2 (not required in mode 1)
        :parm num_rows: number of rows
        :parm num_cols: number of cols

        :parm board: a game board for testing purposes
        """

        if (num_rows < 4) or (num_cols < 4):
            raise Exception("input row or column too small to intialize game")

        self.mode = mode
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.difficulty = difficulty
        self.board = board
        self.p1 = p1
        self.num_empty = None

        if mode == 1:
            self.p2 = COMPUTER_NAME
            self.play = self.single_player()
        elif mode == 2:
            self.p2 = p2
            self.play = self.double_player()
        elif mode == 3:
            self.play = self.ai_vs_ai()

        if not board:
            self.reset()

    def print_board_properties(self):
        print("Board Layout: board[row] [col]")
        print("board[x][0]")
        print("   | board[x][1]")
        print("    |    | board[x][2]")
        print("    |    |    |")
        print("  col1 col2 col3 col4 col5 col6 col7")
        print("[[ 'x', 'x', 'x', 'x', 'x', 'x', 'x'],   row1 -- board[0][x]")
        print(" [ 'x', 'x', 'x', 'x', 'x', 'x', 'x'],   row2 -- board[1][x]")
        print(" [ 'x', 'x', 'x', 'x', 'x', 'x', 'x'],   row3 -- board[2][x]")
        print(" [ 'x', 'x', 'x', 'x', 'x', 'x', 'x'],   row4 -- board[3][x]")
        print(" [ 'x', 'x', 'x', 'x', 'x', 'x', 'x'],   row5 -- board[4][x]")
        print(" [ 'x', 'x', 'x', 'x', 'x', 'x', 'x']]   row6 -- board[5][x]")

    def reset(self):
        """
        Reset board:
          col1 col2 col3 col4 col5 col6 col7
        [[ ' ', ' ', ' ', ' ', ' ', ' ', ' '],   row1
         [ ' ', ' ', ' ', ' ', ' ', ' ', ' '],   row2
         [ ' ', ' ', ' ', ' ', ' ', ' ', ' '],   row3
         [ ' ', ' ', ' ', ' ', ' ', ' ', ' '],   row4
         [ ' ', ' ', ' ', ' ', ' ', ' ', ' '],   row5
         [ ' ', ' ', ' ', ' ', ' ', ' ', ' ']]   row6

        """
        #print([[EMPTY_SLOT]*self.num_cols for i in range (self.num_rows)])
        self.board = [[EMPTY_SLOT]*self.num_cols for i in range(self.num_rows)]
        self.num_empty = self.num_cols * self.num_rows

    def print_game_status(self):
        for i in range (self.num_rows):
            print("    ", end ="")
            for j in range(self.num_cols):
                print("| " + str(self.board[i][j]), end =" ")
            print("|")
        num_str = "   "
        for i in range(1, self.num_cols+1):
            num_str += "   " + str(i)
        print(num_str)

    def next_move(self,round, move):
        """
        :param round: 谁下的棋
        :param move: column the player selected
        :return: None; update the board accordingly or raise Exceptions
        """
        if round == self.p1:
            token = TOKEN_1
        elif round == self.p2:
            token = TOKEN_2
        else:
            raise Exception("No other player exception")

        # Invalid Input
        if move < 0 or move > self.num_cols:
            raise Exception("Invalid column move")
        # Column full
        if self.board[0][move] == EMPTY_SLOT:
            raise Exception("Column Full")
        # Find the bottomist empty slot
        pos = -1
        while pos < self.num_rows - 1 :
            if self.board[pos+1][move] != EMPTY_SLOT:
                break
            pos += 1
        self.board[pos][move] = token
        self.num_empty -= 1

    def line_check(self, token, direction, num=4):
        """
        To check whether 'num' of token are connected together

        :param token: TOKEN_1 or TOKEN_2
        :param direction: 4 direction
        :param num: num of token to check are connected
        :return: boolean
        """
        if direction == "vertical":
            return False
        if direction == "horizontal":
            return False
        if direction == "LD": # from top right to bottom left
            return False
        if direction == "RD": # from top left
            return False


    def single_player(self):
        pass

    def double_player(self):
        pass

    def ai_vs_ai(self):
        pass


if (__name__ == "__main__"):
    game = ConnectFour()
    #game.board[0][4] = "K"
    #game.print_game_status()
    game.print_board_properties()


