from Board import Board
from Board import Card
from copy import deepcopy
from collections import deque
from Solitaire import Solitaire

def dfs(solitaire, num, source = None, isPrint = True):
    if source is None:
        source = solitaire.newGame()
    front = [source]
    parent = {source: None}
    solitaire.__clear_board__(source)
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

class TestDfs:
    def __init__(self):
        self.sol = Solitaire()

    def testNextMoveRandom(self):
        dfs(self.sol, 1000)

    def testNextMove(self):
        board = Board()
        board.tableau = [
                [Card(2,8),Card(2,6),Card(0,9),Card(0,4),Card(3,None)],
                [Card(1,6),Card(1,9),Card(1,1),Card(2,2),Card(2,9)],
                [Card(0,7),Card(5,None),Card(5,None),Card(1,7),Card(1,5)],
                [Card(3,None),Card(1,8),Card(1,3),Card(4,None),Card(0,5)],
                [Card(5,None),Card(4,None),Card(4,None),Card(2,5),Card(0,3)],
                [Card(6,None),Card(5,None),Card(2,3),Card(4,None),Card(1,4)],
                [Card(0,2),Card(2,4),Card(0,8),Card(3,None),Card(3,None)],
                [Card(2,7),Card(2,1),Card(0,1),Card(1,2),Card(0,6)]
                ]
        dfs(self.sol, 60, board)

    def testNextMove2(self):
        board = Board()
        board.tableau = [
                [Card(1,6),Card(1,8),Card(2,2),Card(5,None),Card(1,2)],
                [Card(1,9),Card(0,3),Card(5,None),Card(5,None),Card(1,5)],
                [Card(2,1),Card(3,None),Card(2,5),Card(2,4),Card(0,2)],
                [Card(4,None),Card(3,None),Card(2,7),Card(1,7),Card(2,6)],
                [Card(4,None),Card(0,1),Card(2,8),Card(5,None),Card(0,9)],
                [Card(1,1),Card(1,3),Card(4,None),Card(0,6),Card(2,9)],
                [Card(0,7),Card(6,None),Card(0,5),Card(3,None),Card(1,4)],
                [Card(0,8),Card(0,4),Card(3,None),Card(2,3),Card(4,None)],
                ]
        dfs(self.sol, 2000, board)

    def testNextMove3(self):
        board = Board()
        board.tableau = [
                [Card(1,9),Card(2,2),Card(1,4),Card(2,6),Card(5,None)],
                [Card(5,None),Card(5,None),Card(0,3),Card(2,9),Card(0,7)],
                [Card(4,None),Card(1,7),Card(5,None),Card(3,None),Card(0,9)],
                [Card(2,4),Card(4,None),Card(1,1),Card(0,8),Card(1,6)],
                [Card(1,3),Card(2,1),Card(2,3),Card(0,2),Card(0,6)],
                [Card(0,1),Card(2,7),Card(0,5),Card(3,None),Card(4,None)],
                [Card(1,2),Card(3,None),Card(2,5),Card(1,8),Card(3,None)],
                [Card(1,5),Card(6,None),Card(0,4),Card(4,None),Card(2,8)],
                ]
        dfs(self.sol, 30, board)

    def testSuccessRate(self):
        cnt = 100
        for i in range(100):
            print i
            retval = dfs(self.sol, 2000, isPrint = False)
            if retval is None:
                cnt -= 1
        print cnt / 100.0

if __name__ == "__main__":
    td = TestDfs()
    #td.testNextMoveRandom()
    #td.testNextMove()
    #td.testNextMove2()
    #td.testNextMove3()
    td.testSuccessRate()
