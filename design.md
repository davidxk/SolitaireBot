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

## Heuristic
| Move type | Card | Priority |
|-----------|------|----------|
TAB_TO_FOUND| -    | 4
TAB_TO_STOCK| 箭   | 5
TAB_TO_STOCK| 数   | 9
STOCK_TO_TAB| 箭   | 8
STOCK_TO_TAB|数到数| 0
STOCK_TO_TAB|数到空| 2
STOCK_TO_FOUND| -  | 3
TAB_TO_TAB  |顶到数| 1
TAB_TO_TAB  |下到数| 7
TAB_TO_TAB  |顶到空| 6
TAB_TO_TAB  |下到空| ∞
