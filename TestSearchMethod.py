from Board import Board
from Board import Card
from copy import deepcopy
from collections import deque
from Solitaire import Solitaire
from test_cases import testCases
from TestDepthLimited import depth_limited

def dfs(solitaire, num, source = None, isPrint = True):
    if source is None:
        source = solitaire.newGame()
    solitaire.__clear_board__(source)
    front = [source]
    parent = {source: None}
    cnt = 0
    while front and cnt < num:
        node = front.pop()
        if isPrint:
            print cnt
            print node
        for child in solitaire.nextMove(node):
            solitaire.__clear_board__(child)
            if child not in parent:
                front.append(child)
                parent[child] = node
                if solitaire.isWin(child):
                    return parent, child
        cnt += 1
    return None

class TestSearchMethod:
    def __init__(self, search):
        self.sol = Solitaire()
        self.search = search

    def testNextMoveRandom(self, isPrint = True):
        self.search(self.sol, 1000, isPrint = isPrint)

    def testNextMoveCases(self, i, steps = 2000, isPrint = False):
        board = Board()
        board.tableau = testCases[i - 1]
        #self.search(self.sol, steps, board, isPrint)
        self.search(self.sol, source = board, limit = 50)

    def testSuccessRate(self):
        cnt = 100
        for i in range(100):
            print i
            #retval = self.search(self.sol, 2000, isPrint = False)
            retval = self.search(self.sol, limit = 50)
            if retval is None:
                cnt -= 1
                print "fail"
        print cnt / 100.0

if __name__ == "__main__":
    td = TestSearchMethod(depth_limited)
    #td.testNextMoveRandom(False)
    #td.testNextMoveCases(1)
    #td.testNextMoveCases(2)
    #td.testNextMoveCases(3)
    #td.testNextMoveCases(4)
    #td.testNextMoveCases(5)
    ##td.testNextMoveCases(6)
    #td.testNextMoveCases(7)
    #td.testNextMoveCases(8)
    #td.testNextMoveCases(9)
    td.testSuccessRate()
