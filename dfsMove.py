from copy import deepcopy
from dfs import dfs_wrapper
from SolitaireMove import SolitaireMove

def move_wrapper(solitaire, source = None, isPrint = False):
    return dfs_wrapper(SolitaireMove(), source, isPrint=isPrint, impl = dfsMove)

def dfsMove(solitaire, limit, source = None, isPrint = True):
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
                parent[child] = node
                if solitaire.isWin(child):
                    return parent, child
        cnt += 1
    return None, None

if __name__ == "__main__":
    path = move_wrapper
    if path is None:
        print "Fail"
    else:
        for state in path:
            print state
