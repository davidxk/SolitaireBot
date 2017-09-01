from Solitaire import Solitaire

def dfs(solitaire, limit, source = None, isPrint = True):
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
        for child in solitaire.nextMove(node):
            solitaire.__clear_board__(child)
            if child not in parent:
                front.append(child)
                parent[child] = node
                if solitaire.isWin(child):
                    return parent, child
        cnt += 1
    return None, None

def dfs_wrapper(solitaire, source = None, isPrint = False, impl = dfs):
    parent, target = impl(solitaire, 2000, source, isPrint = isPrint)
    if not parent:
        return None
    node = target
    path = [target]
    while parent[node]:
        path.append(parent[node])
        node = parent[node]
    path.reverse()
    return path

if __name__ == "__main__":
    path = dfs_wrapper(Solitaire())
    if path is None:
        print "Fail"
    else:
        for state in path:
            print state
