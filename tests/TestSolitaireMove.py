from Board import Board
from Board import Card
from copy import deepcopy
from SolitaireMove import SolitaireMove
from Solitaire import find
import unittest

class TestSolitaireMove(unittest.TestCase):
    def setUp(self):
        self.sol = SolitaireMove()
        self.cards = [Card(color, num) for num in range(1, 10) \
                for color in range(3)]
        self.cards += [Card(color, None) for color in range(3, 6) \
                for i in range(4)]
        self.cards += [Card(6, None)]
        self.moves = []

    def testTableauToStock(self):
        board = Board(self.cards)
        self.sol.__getTableauToStock__(board, self.moves)
        self.assertEqual(len(self.moves), 8)
        #for move in self.moves:
            #print self.sol.getChild(deepcopy(board), move)

    def testMovesFromStock(self):
        board = Board(self.cards)
        board.stock[find(board.stock, None)] = board.tableau[-1].pop()
        board.stock[find(board.stock, None)] = board.tableau[-2].pop()
        board.stock[find(board.stock, None)] = board.tableau[-3].pop()
        board.tableau[-1] = []
        self.sol.__getMovesFromStock__(board, self.moves)
        self.assertEqual(len(self.moves), 12)
        #for move in self.moves:
            #print self.sol.getChild(deepcopy(board), move)

    def testTableauToFoundation(self):
        board = Board(self.cards)
        self.sol.__getTableauToFoundation__(board, self.moves)
        self.assertEqual(len(self.moves), 3)
        #for move in self.moves:
            #print self.sol.getChild(deepcopy(board), move)

    def testTableauToTableau(self):
        cards = [Card(color, num) for color in range(3) \
                for num in range(9, 0, -1)]
        cards += [Card(color, None) for color in range(3, 6) \
                for i in range(4)]
        cards += [Card(6, None)]
        board = Board(cards)
        self.sol.__getTableauToTableau__(board, self.moves)
        #for move in sorted(self.moves):
            #print self.sol.getChild(deepcopy(board), move)

    def testTableauToTableauToEmpty(self):
        cards = self.cards
        cards.reverse()
        board = Board(cards)
        board.tableau[0] = []
        self.sol.__getTableauToTableau__(board, self.moves)
        self.assertEqual(len(self.moves), 7)
        #for move in self.moves:
            #print self.sol.getChild(deepcopy(board), move)

    def testTableauToTableauMixed(self):
        board = Board(self.cards)
        for i in range(len(board.tableau)):
            for j in range(i, len(board.tableau[0])):
                board.tableau[i][j], board.tableau[j][i] = \
                        board.tableau[j][i],board.tableau[i][j]
        board.tableau[0] = []
        self.sol.__getTableauToTableau__(board, self.moves)
        self.assertEqual(len(self.moves), 9)
        #for move in sorted(self.moves):
            #print self.sol.getChild(deepcopy(board), move)

    def testNextMove(self):
        board = Board(self.cards)
        print board
        for move in self.sol.nextMove(board):
            print self.sol.getChild(deepcopy(board), move)
