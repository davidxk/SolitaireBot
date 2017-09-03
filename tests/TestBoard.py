from Board import Card
from Board import Board
from Board import OrderedDict
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

class TestOrderedDict(unittest.TestCase):
    def testFoundation(self):
        board = Board()
        found = board.foundation
        self.assertEqual(len(found.color_map), 0)
        found.addToFoundation(1)
        found.addToFoundation(2)
        found.addToFoundation(1)
        self.assertEqual(found.color_map[1], 0)
        self.assertEqual(found.color_map[2], 1)
        self.assertTrue(0 not in found.color_map)
        self.assertEqual(found[1], 2)
        self.assertEqual(found[2], 1)
        found.addToFoundation(0)
        self.assertEqual(found.color_map[0], 2)
        self.assertEqual(found[0], 1)

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
