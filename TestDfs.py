from copy import deepcopy
from collections import deque
from Solitaire import Solitaire

def dfs(solitaire, num):
    source = solitaire.newGame()
    front = [source]
    parent = {source: None}
    solitaire.__clear_board__(source)
    cnt = 0
    while front and cnt < num:
        node = front.pop()
        print node
        if solitaire.isWin(node):
            break
        for child in solitaire.nextMove(node):
            solitaire.__clear_board__(child)
            if child not in parent:
                front.append(child)
                parent[child] = node
        cnt += 1
    return parent, node

class TestDfs:
    def __init__(self):
        self.sol = Solitaire()

    def testNextMove(self):
        dfs(self.sol, 1000)

if __name__ == "__main__":
    td = TestDfs()
    td.testNextMove()
