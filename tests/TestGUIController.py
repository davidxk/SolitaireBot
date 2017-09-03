from Board import Board
from Board import Card
from BestFirstSolitaire import BestFirstSolitaire
from BestFirstSolitaire import TAB_TO_FOUND
from BestFirstSolitaire import TAB_TO_STOCK
from BestFirstSolitaire import STOCK_TO_TAB
from BestFirstSolitaire import STOCK_TO_FOUND
from BestFirstSolitaire import TAB_TO_TAB
from GUIController import GUIController
import time
import unittest
class TestGUIController(unittest.TestCase):
    def setUp(self):
        cards = [Card(color, i) for color in range(3) for i in range(1, 10)]
        cards += [Card(color, None) for color in range(3, 6) for i in range(4)]
        cards.append( Card(6, None) )
        game = Board(cards)
        game.stock[0] = game.tableau[-1].pop()
        game.stock[1] = game.tableau[-2].pop()
        game.stock[2] = game.tableau[-3].pop()
        for i in range(3):
            game.foundation[i] += 1
        print game.foundation.color_map

        self.board = game
        self.ctrl = GUIController()

    def testPressNewGame(self):
        time.sleep(0.5)
        self.ctrl.pressNewGame()
        time.sleep(0.5)

    def testSlayDragon(self):
        for color in range(3, 6):
            self.ctrl.slayDragon(color)
            time.sleep(0.5)

    def testTableauToFoundation(self):
        for i in range(8):
            move = (None, None, TAB_TO_FOUND, i)
            coords = self.ctrl.getCoords[move[2]](self.board, move)
            self.ctrl.dragMouse(coords[0], coords[1])
            time.sleep(0.5)

    def testTableauToStock(self):
        for i in range(8):
            for index in range(3):
                move = (None, None, TAB_TO_STOCK, (i, index))
                coords = self.ctrl.getCoords[move[2]](self.board, move)
                self.ctrl.dragMouse(coords[0], coords[1])
                time.sleep(0.5)

    def testStockToTableau(self):
        for i in range(8):
            move = (None, None, STOCK_TO_FOUND, (i, 0))
            coords = self.ctrl.getCoords[move[2]](self.board, move)
            self.ctrl.dragMouse(coords[0], coords[1])
            time.sleep(0.5)

    def testStockToFoundation(self):
        for index in range(3):
            move = (None, None, STOCK_TO_FOUND, index)
            coords = self.ctrl.getCoords[move[2]](self.board, move)
            self.ctrl.dragMouse(coords[0], coords[1])
            time.sleep(0.5)
