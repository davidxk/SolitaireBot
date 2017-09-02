from copy import deepcopy
from dfs import dfs_wrapper
from BestFirstSolitaire import BestFirstSolitaire

class DFSAgent:
    def __init__(self):
        self.sol = BestFirstSolitaire()

    def getPath(self, source = None, isPrint = False):
        return self.getMoves(source, isPrint, isWithMove = False)

    def getMoves(self, source = None, isPrint = False, isWithMove = True):
        parent, target = self.__dfs__(self.sol, 2000, source, isPrint)
        if not parent:
            return None
        node, move = target, None
        path = []
        while parent[node]:
            node, move = parent[node]
            path.append( (node, move) if isWithMove else node )
        path.reverse()
        return path

    def __dfs__(self, solitaire, limit, source = None, isPrint = True):
        if source is None:
            source = solitaire.newGame()
        solitaire.__clear_board__(source)
        front = [source]
        parent = {source: None}
        cnt = 0
        while front and cnt < limit:
            node = front.pop()
            if isPrint:
                print cnt
                print node
            for move in solitaire.nextMove(node):
                child = solitaire.getChild(deepcopy(node), move)
                solitaire.__clear_board__(child)
                if child not in parent:
                    front.append(child)
                    parent[child] = (node, move)
                    if solitaire.isWin(child):
                        return parent, child
            cnt += 1
        return None, None

if __name__ == "__main__":
    da = DFSAgent()
    path = da.getPath(isPrint = True)
    if path is None:
        print "Fail"
    else:
        for state in path:
            print state
