from Board import Card
from Board import Board
from copy import deepcopy
from random import shuffle

class TestCard:
    def testToString(self):
        for color in range(3):
            for number in range(1, 10):
                print Card(color, number).toString(True)
        for color in range(3, 7):
            print Card(color, None).toString(True)

def dfs(solitaire):
    source = solitaire.newGame()
    stack = [source]
    parent = {source: None}
    cnt = 0
    while stack and cnt < 50:
        node = stack.pop()
        if solitaire.isWin(node):
            break
        for child in solitaire.nextMove(node):
            if child not in parent:
                stack.append(child)
                parent[child] = node
        cnt += 1
    return parent

class TestBoard:
    def __init__(self):
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
        print self.board == grandchild
        print self.board.__hash__()
        print child.__hash__()
        print grandchild.__hash__()
        print len({self.board, grandchild})
        seen = {self.board: 1}
        print grandchild in seen
        print seen[grandchild]

    def testHash2(self):
        parent = dfs(Solitaire())
        

if __name__ == "__main__":
    tc = TestCard()
    tc.testToString()
    tb = TestBoard()
    tb.testStr()
    tb.testHash()
