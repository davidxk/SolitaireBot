from Board import Card
from Board import Board
from copy import deepcopy
from random import shuffle
import unittest

class TestCard(unittest.TestCase):
    def testToString(self):
        for color in range(3):
            for number in range(1, 10):
                print Card(color, number).toString(True)
        for color in range(3, 7):
            print Card(color, None).toString(True)

class TestBoard(unittest.TestCase):
    def setUp(self):
        cards = [Card(color, i) for color in range(3) for i in range(1, 10)]
        cards += [Card(color, None) for color in range(3, 6) for i in range(4)]
        cards.append( Card(6, None) )
        shuffle( cards )
        self.board = Board(cards)

    def testStr(self):
        print self.board

    def testHash(self):
        self.board.stock[0] = self.board.tableau[0].pop()
        child = deepcopy(self.board)
        self.board.tableau[0].append( self.board.stock[0] )
        self.board.stock[0] = None
        grandchild = deepcopy(self.board)

        self.assertEqual( self.board, grandchild )
        self.assertNotEqual( self.board.__hash__(), child.__hash__() )
        self.assertEqual( len({self.board, grandchild}), 1)
        seen = {self.board: 1}
        self.assertTrue( grandchild in seen )

if __name__ == "__main__":
    unittest.main()
