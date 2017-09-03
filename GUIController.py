from BestFirstSolitaire import BestFirstSolitaire
from BestFirstSolitaire import TAB_TO_FOUND
from BestFirstSolitaire import TAB_TO_STOCK
from BestFirstSolitaire import STOCK_TO_TAB
from BestFirstSolitaire import STOCK_TO_FOUND
from BestFirstSolitaire import TAB_TO_TAB
import pyautogui as pag
from time import sleep

class GUIController:
    def __init__(self):
        self.coord = {"Stock": lambda index: (150 * index + 180, 50),
                "Tableau": lambda i, j: (150 * i + 180, 30 * j + 320),
                "Foundation": lambda i: (150 * i + 940, 50),
                "New Game": (1270, 850),
                "Dragon Button": lambda i: (650, 80 * (i-3) + 70)}
        self.getCoords = {
                TAB_TO_FOUND: self.__moveTableauToFoundation__,
                TAB_TO_STOCK: self.__moveTableauToStock__,
                STOCK_TO_TAB: self.__moveStockToTableau__,
                STOCK_TO_FOUND: self.__moveStockToFoundation__,
                TAB_TO_TAB: self.__moveTableauToTableau__
                }
        self.speed = 0.5
        self.sol = BestFirstSolitaire()

    def pressNewGame(self):
        coord = self.coord["New Game"]
        self.clickMouse(coord)
        sleep(4)

    def slayDragon(self, dragon):
        coord = self.coord["Dragon Button"](dragon)
        self.clickMouse(coord)

    def execute(self, path):
        for board, move in path:
            coords = self.getCoords[move[2]](board, move)
            self.dragMouse(coords[0], coords[1])
            dragons, n = self.sol.clearBoard(self.sol.getChild(board, move))
            sleep(n * 0.3)
            for dragon in dragons:
                self.slayDragon(dragon)
        sleep(5)

    def clickMouse(self, coord):
        pag.moveTo(coord[0], coord[1], self.speed, pag.easeInOutQuad)
        pag.mouseDown(x = coord[0], y = coord[1])
        sleep(0.5)
        pag.mouseUp()

    def dragMouse(self, press, release):
        pag.moveTo(press[0], press[1], self.speed, pag.easeInOutQuad)
        pag.dragTo(release[0], release[1], self.speed, pag.easeInOutQuad)

    def __moveTableauToFoundation__(self, board, move):
        i = move[3]
        card = board.tableau[i][-1]
        return self.coord["Tableau"](i, len(board.tableau[i]) - 1), \
            self.coord["Foundation"](board.foundation.color_map[card.color])

    def __moveTableauToStock__(self, board, move):
        i, index = move[3]
        return self.coord["Tableau"](i, len(board.tableau[i]) - 1), \
                self.coord["Stock"](index)

    def __moveStockToTableau__(self, board, move):
        i, index = move[3]
        return self.coord["Stock"](index), \
                self.coord["Tableau"](i, len(board.tableau[i]))

    def __moveStockToFoundation__(self, board, move):
        index = move[3]
        card = board.stock[index]
        return self.coord["Stock"](index), \
            self.coord["Foundation"](board.foundation.color_map[card.color])

    def __moveTableauToTableau__(self, board, move):
        i, j, k = move[3]
        return self.coord["Tableau"](i, j), \
                self.coord["Tableau"](k, len(board.tableau[k]))
