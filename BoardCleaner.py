from collections import defaultdict
class BoardCleaner:
    def clearBoard(self, board):
        self.__clear_flower__(board)
        plan = []
        dragonSlayed = []
        clearedFound = True
        while dragonSlayed or clearedFound:
            clearedFound = self.__clear_foundation__(board)
            self.__clear_flower__(board)
            if not clearedFound:
                dragonSlayed = self.__clear_dragon__(board)
                plan += dragonSlayed
                self.__clear_flower__(board)
            else:
                if not plan or type(plan[-1]) is int:
                    plan.append([0])
                plan[-1][0] += 1
        return plan

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
                if indexInStock[card.color] == -1:
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
                return [color]
        return []

    def __clear_foundation__(self, board):
        minima = min(board.foundation.values())
        colors = filter(lambda x: board.foundation[x] <= minima, range(3))
        for col in board.tableau:
            if col and col[-1].color in colors and \
                    col[-1].number == minima + 1:
                board.foundation.addToFoundation( col[-1].color )
                col.pop()
                return True

        for color in range(3):
            if board.foundation[color] == 1:
                for col in board.tableau:
                    if col and col[-1].color == color and col[-1].number == 2:
                        board.foundation.addToFoundation( col[-1].color )
                        col.pop()
                        return True

        return False
