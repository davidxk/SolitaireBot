
def depth_limited(solitaire, limit = 55, source = None):
    def helper(source, limit, path, result):
        if solitaire.isWin(source):
            result.append(list(path))
            return result
        elif limit <= 0 or source in visited:
            return result
        elif len(visited) > 2500:
            print "Fail"
            result.append(["Fail"])
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
