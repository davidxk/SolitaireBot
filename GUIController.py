import pyautogui as pag

class GUIController:
    def __init__(self):
        self.coord = {"Stock": lambda index: (k * index + b, const),
                "Tableau": lambda i, j: (k * i + b, k * j + b),
                "Foundation": lambda i: (k * i + b, const),
                "New Game": lambda: (x, y)}
        self.getCoords = {
                TAB_TO_FOUND: self.__moveTableauToFoundation__,
                TAB_TO_STOCK: self.__moveTableauToStock__,
                STOCK_TO_TAB: self.__moveStockToTableau__,
                STOCK_TO_FOUND: self.__moveStockToFoundation__,
                TAB_TO_TAB: self.__moveTableauToTableau__
                }
        self.speed = 0.5

    def pressNewGame(self):
        coord = self.coord["New Game"]()
        pag.click(coord[0], coord[1], self.speed, pag.easeInOutQuad)

    def execute(self, path):
        for board, move in path:
            coords = self.getCoords[move[2]](board, move)
            dragMouse(coords[0], coords[1])

    def dragMouse(self, press, release):
        pag.moveTo(press[0], press[1], self.speed, pag.easeInOutQuad)
        pag.dragTo(release[0], release[0], self.speed, pag.easeInOutQuad)

    def __moveTableauToFoundation__(self, board, move):
        i = move[3]
        ("Tableau", i, len(board.tableau[i]) - 1), ("Foundation", card.color)

    def __moveTableauToStock__(self, board, move):
        i, index = move[3]
        ("Tableau", i, len(board.tableau[i]) - 1), ("Stock", index)

    def __moveStockToTableau__(self, board, move):
        i, index = move[3]
        ("Stock", index), ("Tableau", i, len(board.tableau[i]))

    def __moveStockToFoundation__(self, board, move):
        index = move[3]
        ("Stock", index), ("Foundation", card.color)

    def __moveTableauToTableau__(self, board, move):
        i, j, k = move[3]
        ("Tableau", i, j), ("Tableau", k, len(board.tableau[j]))
