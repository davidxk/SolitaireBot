from Board import Board
from Board import Card
from collections import defaultdict
from copy import deepcopy
from random import shuffle

def find(array, elem):
    for i, x in enumerate(array):
        if x == elem:
            return i
    return -1

def isConcatenable(card, head):
    return card.number and head.number and \
            card.number == head.number - 1 and card.color != head.color

# Order: 
# * top tableau to tableau
# * stock to tableau 
# * stock to foundation
# * tableau to foundation
# * tableau dragon to stock
# * tableau lower to tableau
# * tableau number to stock
class Solitaire:
    def __init__(self):
        self.boardCleaner = BoardCleaner()

    def newGame(self):
        cards = [Card(color, i) for color in range(3) for i in range(1, 10)]
        cards += [Card(color, None) for color in range(3, 6) for i in range(4)]
        cards.append( Card(6, None) )
        shuffle( cards )
        game = Board(cards)
        return game
    
    def nextMove(self, board):
        tabToFound                   = self.__getTableauToFoundation__(board)
        draToStock, numToStock            = self.__getTableauToStock__(board)
        stockToTableau, stockToFoundation = self.__getMovesFromStock__(board)
        topTabToTab, lowTabToTab, toEmpty = self.__getTableauToTableau__(board)
        moves = numToStock + lowTabToTab + toEmpty + draToStock + tabToFound + \
                stockToFoundation + topTabToTab + stockToTableau
        return moves

    def __getTableauToFoundation__(self, board):
        moves = []
        for col in board.tableau:
            if col and col[-1].number and \
                    col[-1].number == board.foundation[col[-1].color]+1:
                card = col.pop()
                board.foundation[card.color] += 1
                moves.append(deepcopy(board))
                board.foundation[card.color] -= 1
                col.append(card)
        return moves

    def __getTableauToStock__(self, board):
        dragonToStock, numberToStock = [], []
        index = find(board.stock, None)
        if index >= 0:                  # If there is free space in stock
            for col in board.tableau:   # Find a card to be moved to stack
                if len(col) > 0:
                    card = col.pop()
                    board.stock[index] = card
                    if not card.number: # Dragon
                        dragonToStock.append(deepcopy(board))
                    else:               # Number
                        numberToStock.append(deepcopy(board))
                    col.append(card)    # Recovery
            board.stock[index] = None   # Recovery
        return dragonToStock, numberToStock

    def __getMovesFromStock__(self, board):
        stockToTableau, stockToFoundation = [], []
        for i, card in enumerate(board.stock):
            if card:
                board.stock[i] = None
                # To tableau
                for col in board.tableau:
                    if not col and card.number or \
                            col and isConcatenable(card, col[-1]):
                        col.append(card)
                        stockToTableau.append(deepcopy(board))
                        col.pop()
                # To foundations
                if card.number and \
                        card.number == board.foundation[card.color] + 1:
                    board.foundation[card.color] += 1
                    stockToFoundation.append(deepcopy(board))
                    board.foundation[card.color] -= 1 # recovery
                board.stock[i] = card # recovery
        return stockToTableau, stockToFoundation

    def __getTableauToTableau__(self, board):
        def addMoves(board, col, j, moves, isHead = False):
            card = col[j]
            for k, ncol in enumerate(board.tableau):
                if ncol and isConcatenable(card, ncol[-1]):
                    stack = col[j:]; del col[j:]; ncol += stack
                    moves.append(deepcopy(board))
                    col += stack; del ncol[j - len(col):]
                elif not ncol and j != 0 and isHead:
                    stack = col[j:]; del col[j:]; ncol += stack
                    toEmpty.append(deepcopy(board))
                    col += stack; del ncol[j - len(col):]

        topTabToTab, lowTabToTab, toEmpty = [], [], []
        for i, col in enumerate(board.tableau):
            for j in range(len(col) - 1, -1, -1):
                if j == 0 or not isConcatenable(col[j], col[j - 1]):
                    addMoves(board, col, j, topTabToTab, True)
                    break
                else:
                    addMoves(board, col, j, lowTabToTab)
        return topTabToTab, lowTabToTab, toEmpty

    def __clear_board__(self, board):
        self.boardCleaner.clearBoard(board)

    def isWin(self, board):
        for color in range(3):
            if board.foundation[color] != 9:
                return False
        if board.stock.count([]) < 3:
            return False
        assert board.tableau.count([]) == 8
        return True

class BoardCleaner:
    def clearBoard(self, board):
        self.__clear_flower__(board)
        while self.__clear_dragon__(board) or self.__clear_foundation__(board):
            self.__clear_flower__(board)

    def __clear_flower__(self, board):
        for col in board.tableau:
            if col and col[-1].color == 6:
                col.pop()

    def __clear_dragon__(self, board):
        indexInStock = { color: -1 for color in range(3, 6)}
        stockDragonIndices = defaultdict(list)
        tableauDragonIndices = defaultdict(list)
        for i in range(3):
            card = board.stock[i]
            if card is None:
                for color in indexInStock:
                    if indexInStock[color] == -1:
                        indexInStock[color] = i
            elif card and card.number is None: # Flower cleared, must be Dragon
                stockDragonIndices[card.color].append(i)
                indexInStock[card.color] = i

        for i, col in enumerate(board.tableau):
            if col and col[-1].number is None:
                tableauDragonIndices[col[-1].color].append(i)

        for color in range(3, 6):
            if indexInStock[color] >= 0 and len(stockDragonIndices[color]) + \
                    len(tableauDragonIndices[color]) == 4:
                for i in stockDragonIndices[color]:
                    board.stock[i] = None
                for i in tableauDragonIndices[color]:
                    board.tableau[i].pop()
                board.stock[indexInStock[color]] = []
                return True
        return False

    def __clear_foundation__(self, board):
        minima = min(board.foundation.values())
        colors = filter(lambda x: board.foundation[x] <= minima, range(3))
        for col in board.tableau:
            if col and col[-1].color in colors and \
                    col[-1].number == minima + 1:
                board.foundation[col[-1].color] += 1
                col.pop()
                return True

        for color in range(3):
            if board.foundation[color] == 1:
                for col in board.tableau:
                    if col and col[-1].color == color and col[-1].number == 2:
                        board.foundation[col[-1].color] += 1
                        col.pop()
                        return True

        return False
