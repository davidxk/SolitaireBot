from Board import Board
from Solitaire import Solitaire
from Solitaire import find
from Solitaire import isAppendable
from Solitaire import canAddToFoundation

TAB_TO_FOUND = 0
TAB_TO_STOCK = 1
STOCK_TO_TAB = 2
STOCK_TO_FOUND = 3
TAB_TO_TAB = 4

prt = { TAB_TO_FOUND: 4,
        TAB_TO_STOCK: {color: 9 if color < 3 else 5 for color in range(6)},
        STOCK_TO_TAB: {color: 0 if color < 3 else 8 for color in range(6)},
        STOCK_TO_FOUND: 3,
        TAB_TO_TAB: {True: 1, False: 7} }


class SolitaireMove(Solitaire):
    def __init__(self):
        super(SolitaireMove, self).__init__()
        self.cardmover = CardMover()

    def nextMove(self, board):
        moves = []
        self.__getTableauToFoundation__(board, moves)
        self.__getTableauToStock__(board, moves)
        self.__getMovesFromStock__(board, moves)
        self.__getTableauToTableau__(board, moves)
        moves.sort(reverse = True)
        return moves

    def __getTableauToFoundation__(self, board, moves):
        for i, col in enumerate(board.tableau):
            if col and canAddToFoundation(board, col[-1]): 
                moves.append( (prt[TAB_TO_FOUND], 0, TAB_TO_FOUND, i) )

    def __getTableauToStock__(self, board, moves):
        index = find(board.stock, None)
        if index < 0:        # If there is no free space in stock, return
            return
        for i, col in enumerate(board.tableau): 
            if len(col) > 0:
                card = col[-1]
                move = [prt[TAB_TO_STOCK][card.color]]
                move += [self.__getDragonToStockPriority__(board, card)]
                move += [TAB_TO_STOCK, (i, index)]
                moves.append( tuple(move) )

    def __getMovesFromStock__(self, board, moves):
        for index, card in enumerate(board.stock):
            if card:
                # To tableau
                for i, col in enumerate(board.tableau):
                    if not col and card.number: # Number to empty column
                        moves.append( (2, 0, STOCK_TO_TAB, (i, index)) )
                    elif col and isAppendable(card, col[-1]): # Number append
                        moves.append( (0, 0, STOCK_TO_TAB, (i, index)) )
                # To foundations
                if canAddToFoundation(board, card):
                    moves.append( (prt[STOCK_TO_FOUND], 0, STOCK_TO_FOUND,
                        index) )

    def __getTableauToTableau__(self, board, moves):
        def addMoves(board, col, j, isHead):
            card = col[j]
            for k, ncol in enumerate(board.tableau):
                if ncol and isAppendable(card, ncol[-1]):
                    moves.append( (prt[TAB_TO_TAB][isHead], 0, 
                        TAB_TO_TAB, (i, j, k)) )
                elif not ncol and j != 0 and isHead:
                    moves.append( (6, 0, TAB_TO_TAB, (i, j, k)) )

        for i, col in enumerate(board.tableau):
            for j in range(len(col) - 1, -1, -1):
                if j == 0 or not isAppendable(col[j], col[j - 1]):
                    addMoves(board, col, j, True)
                    break
                else:
                    addMoves(board, col, j, False)

    def __getDragonToStockPriority__(self, board, card):
        if card.number:
            return 0
        prt = 0
        for col in board.tableau:
            for i in range(len(col)):
                if col[i].color == card.color:
                    for j in range(i+1, len(col)):
                        if not isAppendable(col[j], col[j - 1]):
                            prt += 1
                    break
        return prt

    def getChild(self, node, move):
        self.cardmover.makeMove(node, move)
        return node

class CardMover:
    def __init__(self):
        self.moveFunc = {
                TAB_TO_FOUND: self.__moveTableauToFoundation__,
                TAB_TO_STOCK: self.__moveTableauToStock__,
                STOCK_TO_TAB: self.__moveStockToTableau__,
                STOCK_TO_FOUND: self.__moveStockToFoundation__,
                TAB_TO_TAB: self.__moveTableauToTableau__
                }

    def makeMove(self, board, move):
        self.moveFunc[move[2]](board, move)

    def __moveTableauToFoundation__(self, board, move):
        i = move[3]
        card = board.tableau[i].pop()
        board.foundation[card.color] += 1

    def __moveTableauToStock__(self, board, move):
        i, index = move[3]
        card = board.tableau[i].pop()
        board.stock[index] = card

    def __moveStockToTableau__(self, board, move):
        i, index = move[3]
        card = board.stock[index]
        board.stock[index] = None
        board.tableau[i].append(card)

    def __moveStockToFoundation__(self, board, move):
        index = move[3]
        card = board.stock[index]
        board.stock[index] = None
        board.foundation[card.color] += 1

    def __moveTableauToTableau__(self, board, move):
        i, j, k = move[3]
        col, ncol = board.tableau[i], board.tableau[k]
        stack = col[j:]
        del col[j:]
        ncol += stack
