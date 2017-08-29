from Board import Board
from Board import Card
from copy import deepcopy
from collections import deque
from Solitaire import Solitaire
from test_cases import testCases
from TestDepthLimited import depth_limited
from dfs import dfs_wrapper

class TestSearchMethod:
    def __init__(self, search):
        self.sol = Solitaire()
        self.search = search

    def testNextMoveRandom(self):
        self.search(self.sol)

    def testNextMoveCases(self, i):
        board = Board()
        board.tableau = testCases[i - 1]
        self.search(self.sol, source = board)

    def testSuccessRate(self):
        cnt = 100
        for i in range(100):
            print i
            path = self.search(self.sol)
            if path is None:
                cnt -= 1
                print "fail"
        print cnt, "%"

    def getAverageDepth(self):
        cnt, totalLenth, maximum = 0, 0, 0
        for i in range(100):
            path = dfs_wrapper(self.sol)
            if path is not None:
                cnt += 1; totalLenth += len(path)
                maximum = max(len(path), maximum)
        print cnt
        print 1.0 * totalLenth / cnt
        print maximum

if __name__ == "__main__":
    td = TestSearchMethod(dfs_wrapper)
    td.testNextMoveRandom()
    td.testNextMoveCases(1)
    #td.testNextMoveCases(2)
    #td.testNextMoveCases(3)
    #td.testNextMoveCases(4)
    #td.testNextMoveCases(5)
    ##td.testNextMoveCases(6)
    #td.testNextMoveCases(7)
    #td.testNextMoveCases(8)
    #td.testNextMoveCases(9)
    #td.testSuccessRate()
    #td.getAverageDepth()
