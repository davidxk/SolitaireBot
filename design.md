# Class
## Solitaire Bot
+ dfs

## Solitaire: Search Problem
+ new game: None -> board
+ next move: board -> [board]
- clear board: board -> board
+ is win: board -> bool

## Board Cleaner: helper class
+ clear board: board -> board

## Board: State
* stock: set()
* tableau: [[]]
* foundation: dict(color: number)
+ \_\_init\_\_
- \_\_str\_\_
- \_\_unicode\_\_
- \_\_hash\_\_

## Card
* color: 0饼, 1条, 2万, 3中, 4发, 5白, 6花
* number: 1-9, None
+ toString

<!-- red:"饼", green:"条", white:"万", red:"中", green:"发", white:"白", magenta:"花" -->
