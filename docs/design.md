# Algorithm Prototype Design
## Solitaire Bot
+ dfs
+ dfs wrapper

## Solitaire: Search Problem
+ new game: None -> board
+ next move: board -> [board]
+ clear board: board -> board
+ is win: board -> bool

## Board Cleaner: helper class
+ clear board: board -> board
+ clear and get: board -> board, foundation:{color: index}, dragon: [color]

## Board: State
* stock: []
* tableau: [[]]
* foundation: dict(color: number)
+ \_\_init\_\_
- \_\_str\_\_: for printing
- \_\_unicode\_\_: for printing
- \_\_repr\_\_: for debugging
- \_\_hash\_\_: for hashing
- \_\_eq\_\_: for hashing

## Card
* color: 0饼, 1条, 2万, 3中, 4发, 5白, 6花
* number: 1-9, None
+ toString
- \_\_repr\_\_: for hashing
- \_\_eq\_\_: for hashing

<!-- red:"饼", green:"条", white:"万", red:"中", green:"发", white:"白", magenta:"花" -->

# Bot Design
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

## Screen Parser
+ parse_screenshot: png image -> board
+ save_screenshot: screen -> png image

## DFS Agent
+ get path: solitaire, board -> [(node, move)]
+ get moves: solitaire, board -> [move]
- \_\_dfs\_\_: solitaire, board -> {child: node, move}

## Best First Solitaire
+ next move: board -> [move]

## Move
+ priority
+ type
+ parameters
- \_\_lt\_\_: for sorting
- \_\_str\_\_: for printing

## Card Mover
+ init foundation
+ make move: board, move -> board

## GUI Controller
+ foundation map
- init foundation: board -> foundation map
- update foundation: ? -> foundation map
+ execute: [node, move]
+ press New Game
