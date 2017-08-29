from Board import Board
from Board import Card
from Solitaire import find
from Solitaire import Solitaire
import unittest

class TestSolitaire(unittest.TestCase):
    def setUp(self):
        self.sol = Solitaire()
        self.cards = [Card(color, num) for num in range(1, 10) \
                for color in range(3)]
        self.cards += [Card(color, None) for color in range(3, 6) \
                for i in range(4)]
        self.cards += [Card(6, None)]

    def testIsWin(self):
        state = Board()
        state.stock = [[] for i in range(3)]
        state.foundation = { color: 9 for color in range(3) }
        self.assertTrue( self.sol.isWin(state) )
        self.assertFalse( self.sol.isWin(Board(self.cards)) )

    def testTableauToStock(self):
        game = Board(self.cards)
        moves = self.sol.__getTableauToStock__(game)
        for move in moves:
            print move

    def testMovesFromStock(self):
        game = Board(self.cards)
        game.stock[find(game.stock, None)] = game.tableau[-1].pop()
        game.stock[find(game.stock, None)] = game.tableau[-2].pop()
        game.stock[find(game.stock, None)] = game.tableau[-3].pop()
        game.tableau[-1] = []
        print game
        for move in self.sol.nextMove(game):
            print move

    def testTableauToFoundation(self):
        game = Board(self.cards)
        moves = self.sol.__getTableauToFoundation__(game)
        for move in moves:
            print move

    def testTableauToTableau(self):
        cards = [Card(color, num) for color in range(3) \
                for num in range(9, 0, -1)]
        cards += [Card(color, None) for color in range(3, 6) \
                for i in range(4)]
        cards += [Card(6, None)]
        game = Board(copy(cards))
        print game
        a, b = self.sol.__getTableauToTableau__(game)
        for move in a + b:
            print move

    def testTableauToTableau2(self):
        cards = self.cards
        cards.reverse()
        game = Board(cards)
        game.tableau[0] = []
        print game
        a, b = self.sol.__getTableauToTableau__(game)
        for move in a + b:
            print move

    def testTableauToTableau3(self):
        game = Board(self.cards)
        for i in range(len(game.tableau)):
            for j in range(i, len(game.tableau[0])):
                game.tableau[i][j], game.tableau[j][i] = \
                        game.tableau[j][i],game.tableau[i][j]
        game.tableau[0] = []
        print game
        a, b = self.sol.__getTableauToTableau__(game)
        for move in a + b:
            print move

    def testNextMove(self):
        game = Board(self.cards)
        print game
        for move in self.sol.nextMove(game):
            print move

    def testNextMove2(self):
        cards = [Card(color, num) for color in range(3) \
                for num in range(9, 0, -1)]
        cards += [Card(color, None) for color in range(3, 6) \
                for i in range(4)]
        cards += [Card(6, None)]
        game = Board(copy(cards))
        print game
        for move in self.sol.nextMove(game):
            print move

    def testNextMoveRandom(self):
        game = self.sol.newGame()
        print game
        for move in self.sol.nextMove(game):
            print move

    def testNextMoveFinishing(self):
        game = Board()
        game.stock = [[], None, []]
        game.tableau = [[Card(0, 9)], [Card(5, None), Card(2, 7), Card(2, 8)],
                [Card(5, None)], [Card(5, None)], [], [], [Card(2, 9)], [Card(5, None)]]
        game.foundation = {0: 8, 1: 9, 2: 6}
        print game
        for move in self.sol.nextMove(game):
            print move

    def testNextMoveFinishing2(self):
        game = Board()
        game.stock = [None, [], []]
        game.tableau = [[Card(1, 9), Card(3, None), Card(0, 9), Card(1, 8), 
                Card(2, 7)],
                [Card(3, None)], [Card(3, None)], [], [Card(2, 5), Card(2, 8)],
                [], [Card(3, None)], [Card(2, 9), Card(0, 8), Card(1, 7), 
                Card(2, 6)]]
        game.foundation = {0: 7, 1: 6, 2: 4}
        print game
        for move in self.sol.nextMove(game):
            print move

    def testNextMoveFinishing3(self):
        game = Board()
        game.stock = [[], [], []]
        game.tableau = [[], [Card(0, 9), Card(0, 7)], [Card(2, 3), Card(1, 6)],
                [Card(2, 5), Card(0, 4)], [],
                [Card(2, 9), Card(0, 8), Card(2, 7), Card(0, 6), Card(1, 5), Card(2, 4)], 
                [Card(1, 8)], 
                [Card(1, 9), Card(2, 8), Card(1, 7), Card(2, 6), Card(0, 5), Card(1, 4)]]
        game.foundation = {0: 3, 1: 3, 2: 2}
        print game
        for move in self.sol.nextMove(game):
            print move

    def testNextMoveFinishing4(self):
        game = Board()
        game.stock = [[], [], []]
        game.tableau = [[Card(1, 5), Card(1, 7)], [Card(0, 9), Card(1, 8), Card(2, 7), Card(1, 6)], 
                [], [Card(1, 9), Card(2, 8), Card(0, 7), Card(1, 6)], [Card(2, 9), Card(0, 8)],
                [], [], []]
        game.foundation = {0: 6, 1: 4, 2: 5}
        print game
        for move in self.sol.nextMove(game):
            print move

if __name__ == "__main__":
    ts = TestSolitaire()
    #ts.testIsWin()
    #ts.testTableauToStock()
    #ts.testMovesFromStock()
    #ts.testTableauToFoundation()
    #ts.testTableauToTableau()
    #ts.testTableauToTableau2()
    #ts.testTableauToTableau3()
    #ts.testNextMove()
    #ts.testNextMove2()
    #ts.testNextMoveRandom()
    #ts.testNextMoveFinishing()
    #ts.testNextMoveFinishing2()
    #ts.testNextMoveFinishing3()
    #ts.testNextMoveFinishing4()
