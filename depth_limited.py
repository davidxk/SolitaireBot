from copy import deepcopy
from collections import deque
from Solitaire import Solitaire

def iterative_deepening(solitaire, source=None, min_depth=35, max_depth=100):
    for limit in range(min_depth, max_depth + 1):
        result = depth_limited(solitaire, limit, source)
        if result:
            return result

def depth_limited(solitaire, limit = 55, source = None):
    def helper(source, limit, path, result):
        if solitaire.isWin(source):
            result.append(list(path))
            return result
        elif limit <= 0 or source in visited:
            return result
        visited.add(source)
        moves = solitaire.nextMove(source)
        moves.reverse()
        for child in moves:
            solitaire.clearBoard(child)
            path.append(child)
            if helper(child, limit - 1, path, result):
                return result
            path.pop()
        return result

    if source is None:
        source = solitaire.newGame()
    solitaire.clearBoard(source)
    visited = set()
    return helper(source, limit, [source], [])

if __name__ == "__main__":
    result = iterative_deepening(Solitaire(), min_depth = 35, max_depth = 50)
    for node in result.pop():
        print node
