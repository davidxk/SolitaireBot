from Board import Board
from Board import Card
from copy import copy
from Solitaire import find
from Solitaire import Solitaire

class TestSolitaire:
    def __init__(self):
        self.sol = Solitaire()
        self.cards = [Card(color, num) for num in range(1, 10) \
                for color in range(3)]
        self.cards += [Card(color, None) for color in range(3, 6) \
                for i in range(4)]
        self.cards += [Card(6, None)]

    def testIsWin(self):
        state = Board()
        state.stock = [[] * 3]
        state.foundation = { color: 9 for color in range(3) }
        print self.sol.isWin(state)

    def testTableauToStock(self):
        game = Board(copy(self.cards))
        moves = []
        self.sol.__getTableauToStock__(game, moves)
        for move in moves:
            print move

    def testMovesFromStock(self):
        game = Board(copy(self.cards))
        game.stock[find(game.stock, None)] = game.tableau[-1].pop()
        game.stock[find(game.stock, None)] = game.tableau[-2].pop()
        game.stock[find(game.stock, None)] = game.tableau[-3].pop()
        game.tableau[-1] = []
        print game
        for move in self.sol.nextMove(game):
            print move

    def testTableauToFoundation(self):
        game = Board(copy(self.cards))
        moves = []
        self.sol.__getTableauToFoundation__(game, moves)
        for move in moves:
            print move

    def testTableauToTableau(self):
        game = Board(copy(self.cards))
        moves = []
        print game
        self.sol.__getTableauToTableau__(game, moves)
        for move in moves:
            print move

    def testNextMove(self):
        game = Board(copy(self.cards))
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


if __name__ == "__main__":
    ts = TestSolitaire()
    ts.testIsWin()
    #ts.testTableauToStock()
    #ts.testMovesFromStock()
    #ts.testTableauToFoundation()
    #ts.testTableauToTableau()
    ts.testNextMove()
    ts.testNextMove2()
