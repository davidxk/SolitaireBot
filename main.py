from sys import argv
from dfs import dfs_wrapper
from screenparser import ScreenParser
from Solitaire import Solitaire

if __name__ == "__main__":
    parser = ScreenParser()
    board = parser.parse_screenshot(argv.pop())
    print "Parsed board:"
    print board
    path = dfs_wrapper(Solitaire(), board)
    for state in path:
        print state
