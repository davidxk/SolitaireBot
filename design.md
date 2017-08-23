# Class
## Solitaire Bot
* dfs

## Solitaire: Search Problem
+ new game: None -> board
+ next move: board -> [board]
+ is win: board -> bool

## Board: State
* stock: set()
* tableau: [[]]
* foundation: dict(type: number)
+ \_\_init\_\_
- \_\_str\_\_
- \_\_hash\_\_

## Card
* type: 0饼, 1条, 2万, 3中, 4发, 5白, 6花
* number: 1-9, None
- \_\_str\_\_
+ \_\_concatenable\_\_(self, card, head):
+ \_\_successive\_\_(self, card, foundation):
