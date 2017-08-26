from Board import Board
from Board import Card
from copy import copy
from Solitaire import BoardCleaner

class TestBoardCleaner:
    def __init__(self):
        self.bc = BoardCleaner()
        self.cards = [Card(color, num) for num in range(1, 10) \
                for color in range(3)]
        self.cards += [Card(color, None) for color in range(3, 6) \
                for i in range(4)]
        self.cards += [Card(6, None)]

    def testClearFunctions(self):
        board = Board(copy(self.cards))
        print board
        if not self.bc.flowerCleared:
            if self.bc.__clear_flower__(board):
                print board
        hasChange = True
        while hasChange:
            hasChange = False
            if self.bc.__clear_dragon__(board):
                hasChange = True
                print board
            if self.bc.__clear_foundation__(board):
                hasChange = True
                print board
            if not self.bc.flowerCleared:
                if self.bc.__clear_flower__(board):
                    print board

    def testClearBoard(self):
        board = Board(copy(self.cards))
        print board
        self.bc.clearBoard(board)
        print board

if __name__ == "__main__":
    tbc = TestBoardCleaner()
    tbc.testClearBoard()
