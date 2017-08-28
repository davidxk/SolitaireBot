from copy import deepcopy
from collections import deque
from Solitaire import Solitaire

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
            solitaire.__clear_board__(child)
            path.append(child)
            if helper(child, limit - 1, path, result):
                return result
            path.pop()
        return result

    if source is None:
        source = solitaire.newGame()
    solitaire.__clear_board__(source)
    visited = set()
    return helper(source, limit, [source], [])

if __name__ == "__main__":
    result = depth_limited(Solitaire(), 55)
    for node in result.pop():
        print node
