from copy import deepcopy
from collections import deque
from Solitaire import Solitaire

def dfs(solitaire):
    source = solitaire.newGame()
    solitaire.__clear_board__(source)
    front = [source]
    parent = {source: None}
    while front:
        node = front.pop()
        if solitaire.isWin(node):
            break
        for child in solitaire.nextMove(node):
            solitaire.__clear_board__(child)
            if child not in parent:
                front.append(child)
                parent[child] = node
    return parent, node

def bfs(solitaire):
    source = solitaire.newGame()
    front = deque([source])
    parent = {source: None}
    solitaire.__clear_board__(source)
    while front:
        node = front.popleft()
        #print node
        if solitaire.isWin(node):
            break
        for child in solitaire.nextMove(node):
            solitaire.__clear_board__(child)
            if child not in parent:
                front.append(child)
                parent[child] = node
    return parent, node

if __name__ == "__main__":
    parent, target = dfs(Solitaire())
    print target in parent
    node = target
    print node in parent
    path = [target]
    while parent[node]:
        path.append(parent[node])
        node = parent[node]
    path.reverse()
    for state in path:
        print state
